"""
Controle de alto nível da Matribox II Pro.

Este módulo oferece métodos com nomes claros, como ligar e desligar o
afinador, sem exigir que o usuário da biblioteca conheça números de
Control Change ou valores MIDI.
"""

from __future__ import annotations

from types import TracebackType

from .commands import ControlChange, EffectModule, OperatingModeValue, StompControl, SwitchValue
from .midi_output import MatriboxMidiOutput


class MatriboxController:
    """
    Interface principal para controlar a Matribox II Pro.

    Esta classe utiliza MatriboxMidiOutput para realizar a comunicação MIDI,
    mas apresenta comandos mais fáceis de compreender.

    Exemplo:
        with MatriboxController() as matribox:
            matribox.tuner_on()
            matribox.tuner_off()
    """

    def __init__(self, port_name: str | None = None) -> None:
        """
        Inicializa o controlador da pedaleira.

        Args:
            port_name:
                Nome completo da porta MIDI.

                Quando não é informado, a porta da Matribox é localizada
                automaticamente.
        """
        self._midi_output = MatriboxMidiOutput(port_name)

    @property
    def is_connected(self) -> bool:
        """Informa se a conexão MIDI está aberta."""
        return self._midi_output.is_connected

    @property
    def port_name(self) -> str | None:
        """Retorna o nome da porta MIDI atualmente conectada."""
        return self._midi_output.port_name

    def connect(self) -> str:
        """
        Abre a conexão MIDI com a Matribox.

        Returns:
            Nome completo da porta MIDI aberta.
        """
        return self._midi_output.connect()

    def disconnect(self) -> None:
        """Fecha a conexão MIDI com a Matribox."""
        self._midi_output.disconnect()

    def select_program(self, program: int) -> None:
        """
        Seleciona um programa ou preset por meio de Program Change.

        Args:
            program:
                Número MIDI do programa, entre 0 e 127.

                O número 0 representa o primeiro programa MIDI,
                o número 1 representa o segundo, e assim por diante.
        """
        self._midi_output.send_program_change(program) 


    def select_preset(self, bank: int, preset: str) -> None:
        """
        Seleciona um preset utilizando o número do banco e uma letra.

        Exemplos:
            select_preset(1, "A") seleciona 01A.
            select_preset(32, "C") seleciona 32C.
            select_preset(60, "D") seleciona 60D.

        Args:
            bank:
                Número do banco, entre 1 e 60.

            preset:
                Letra do preset: A, B, C ou D.

        Raises:
            ValueError:
                Quando o banco ou a letra do preset são inválidos.
        """
        if not 1 <= bank <= 60:
            raise ValueError("O banco deve estar entre 1 e 60.")

        preset_name = preset.strip().upper()

        preset_positions = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
        }

        if preset_name not in preset_positions:
            raise ValueError("O preset deve ser A, B, C ou D.")

        if bank <= 30:
            bank_select = 0
            local_bank = bank
        else:
            bank_select = 1
            local_bank = bank - 30

        program = (
            ((local_bank - 1) * 4)
            + preset_positions[preset_name]
        )

        self._midi_output.send_control_change(
            ControlChange.BANK_SELECT,
            bank_select,
        )

        self.select_program(program)       

    def bank_up(self) -> None:
        """Avança para o próximo banco da Matribox II Pro."""
        self._midi_output.send_control_change(
            ControlChange.BANK_UP,
            SwitchValue.ON,
        )

    def bank_down(self) -> None:
        """Retorna para o banco anterior da Matribox II Pro."""
        self._midi_output.send_control_change(
            ControlChange.BANK_DOWN,
            SwitchValue.ON,
        )

    def next_preset(self) -> None:
        """Avança para o próximo preset."""
        self._midi_output.send_control_change(
            ControlChange.PRESET_NEXT,
            SwitchValue.ON,
        )

    def previous_preset(self) -> None:
        """Retorna para o preset anterior."""
        self._midi_output.send_control_change(
            ControlChange.PRESET_PREVIOUS,
            SwitchValue.ON,
        )

    def set_preset_volume(self, volume: int) -> None:
        """
        Define o volume do preset atual.

        Args:
            volume:
                Valor do volume MIDI, entre 0 e 127.

                0 representa o volume mínimo.
                127 representa o volume máximo.

        Raises:
            ValueError:
                Quando o volume está fora do intervalo permitido.
        """
        if not 0 <= volume <= 127:
            raise ValueError(
                "O volume do preset deve estar entre 0 e 127."
            )

        self._midi_output.send_control_change(
            ControlChange.PRESET_VOLUME,
            volume,
        )

    def set_expression(self, value: int) -> None:
        """
        Define o valor do controle de expressão do preset atual.

        Args:
            value:
                Valor MIDI entre 0 e 127.

                O efeito produzido depende de qual parâmetro está associado
                ao pedal de expressão dentro do preset atual.

        Raises:
            ValueError:
                Quando o valor está fora do intervalo permitido.
        """
        if not 0 <= value <= 127:
            raise ValueError(
                "O valor de expressão deve estar entre 0 e 127."
            )

        self._midi_output.send_control_change(
            ControlChange.EXPRESSION,
            value,
        )

    def select_expression_a(self) -> None:
        """Seleciona a configuração A do pedal de expressão interno."""
        self._midi_output.send_control_change(
            ControlChange.EXPRESSION_1_A_B,
            SwitchValue.OFF,
        )

    def select_expression_b(self) -> None:
        """Seleciona a configuração B do pedal de expressão interno."""
        self._midi_output.send_control_change(
            ControlChange.EXPRESSION_1_A_B,
            SwitchValue.ON,
        )                

    def preset_mode(self) -> None:
        """
        Ativa o modo Preset da Matribox II Pro.

        Nesse modo, os quatro footswitches principais selecionam
        os presets A, B, C e D do banco atual.
        """
        self._midi_output.send_control_change(
            ControlChange.PRESET_STOMP_MODE,
            OperatingModeValue.PRESET,
        )

    def stomp_mode(self) -> None:
        """
        Ativa o modo Stomp da Matribox II Pro.

        Nesse modo, os quatro footswitches principais executam as ações
        configuradas no preset atual, como ligar ou desligar efeitos.
        """
        self._midi_output.send_control_change(
            ControlChange.PRESET_STOMP_MODE,
            OperatingModeValue.STOMP,
        )

    def stomp_control_on(self, control: StompControl) -> None:
        """
        Ativa o controle configurável indicado no modo Stomp.

        A ação executada depende da configuração do preset atual. Um controle
        pode ligar um único efeito ou vários módulos ao mesmo tempo.

        Args:
            control:
                Controle configurável, entre CONTROL_1 e CONTROL_4.
        """
        self._midi_output.send_control_change(
            control,
            SwitchValue.ON,
        )

    def stomp_control_off(self, control: StompControl) -> None:
        """
        Desativa o controle configurável indicado no modo Stomp.

        Args:
            control:
                Controle configurável, entre CONTROL_1 e CONTROL_4.
        """
        self._midi_output.send_control_change(
            control,
            SwitchValue.OFF,
        )

    def tap_tempo(self) -> None:
        """
        Envia uma batida do Tap Tempo para a Matribox II Pro.

        O comando envia o pressionamento e a liberação do controle para que
        chamadas consecutivas sejam reconhecidas como batidas separadas.
        """
        self._midi_output.send_control_change(
            ControlChange.TAP_TEMPO,
            SwitchValue.ON,
        )

        self._midi_output.send_control_change(
            ControlChange.TAP_TEMPO,
            SwitchValue.OFF,
        )

    def set_bpm(self, bpm: int) -> None:
        """
        Define diretamente o BPM do preset atual.

        A Matribox utiliza dois comandos MIDI para representar valores
        entre 40 e 300 BPM:

        - CC 68 envia a parte superior do valor;
        - CC 69 envia a parte restante.

        Args:
            bpm:
                Andamento desejado, entre 40 e 300 BPM.

        Raises:
            ValueError:
                Quando o BPM está fora do intervalo permitido.
        """
        if not 40 <= bpm <= 300:
            raise ValueError(
                "O BPM deve estar entre 40 e 300."
            )

        if bpm <= 127:
            bpm_msb = 0
            bpm_lsb = bpm
        elif bpm <= 255:
            bpm_msb = 1
            bpm_lsb = bpm - 128
        else:
            bpm_msb = 2
            bpm_lsb = bpm - 256

        self._midi_output.send_control_change(
            ControlChange.PRESET_BPM_MSB,
            bpm_msb,
        )

        self._midi_output.send_control_change(
            ControlChange.PRESET_BPM_LSB,
            bpm_lsb,
        )

    def looper_on(self) -> None:
        """Abre e ativa o Looper da Matribox II Pro."""
        self._midi_output.send_control_change(
            ControlChange.LOOPER,
            SwitchValue.ON,
        )

    def looper_off(self) -> None:
        """Fecha e desativa o Looper da Matribox II Pro."""
        self._midi_output.send_control_change(
            ControlChange.LOOPER,
            SwitchValue.OFF,
        )

    def looper_record(self) -> None:
        """Inicia a gravação de um loop."""
        self._midi_output.send_control_change(
            ControlChange.LOOPER_RECORD,
            SwitchValue.ON,
        )

    def looper_auto_record(self) -> None:
        """
        Prepara o Looper para iniciar a gravação automaticamente.

        A gravação deve começar quando a Matribox detectar o sinal
        do instrumento.
        """
        self._midi_output.send_control_change(
            ControlChange.LOOPER_AUTO_RECORD,
            SwitchValue.ON,
        )

    def looper_play(self) -> None:
        """Reproduz o loop gravado."""
        self._midi_output.send_control_change(
            ControlChange.LOOPER_PLAY_STOP,
            SwitchValue.ON,
        )

    def looper_stop(self) -> None:
        """Interrompe a reprodução ou gravação do loop."""
        self._midi_output.send_control_change(
            ControlChange.LOOPER_PLAY_STOP,
            SwitchValue.OFF,
        )

    def looper_delete(self) -> None:
        """Apaga a gravação atualmente armazenada no Looper."""
        self._midi_output.send_control_change(
            ControlChange.LOOPER_DELETE,
            SwitchValue.ON,
        )


    def looper_undo_redo(self) -> None:
        """
        Desfaz ou refaz a última camada de overdub do Looper.

        A primeira chamada desfaz a última camada adicionada.
        Uma nova chamada refaz essa mesma camada.
        """
        self._midi_output.send_control_change(
            ControlChange.LOOPER_UNDO_REDO,
            SwitchValue.ON,
        )

    def tuner_on(self) -> None:
        """Liga o afinador da Matribox II Pro."""
        self._midi_output.send_control_change(
            ControlChange.TUNER,
            SwitchValue.ON,
        )

    def tuner_off(self) -> None:
        """Desliga o afinador da Matribox II Pro."""
        self._midi_output.send_control_change(
            ControlChange.TUNER,
            SwitchValue.OFF,
        )

    def effect_module_on(self, module: EffectModule) -> None:
        """
        Liga um módulo de efeito da Matribox II Pro.

        Args:
            module:
                Módulo que deverá ser ligado, entre MODULE_1 e MODULE_12.
        """
        self._midi_output.send_control_change(
            module,
            SwitchValue.ON,
        )

    def effect_module_off(self, module: EffectModule) -> None:
        """
        Desliga um módulo de efeito da Matribox II Pro.

        Args:
            module:
                Módulo que deverá ser desligado, entre MODULE_1 e MODULE_12.
        """
        self._midi_output.send_control_change(
            module,
            SwitchValue.OFF,
        )

    def __enter__(self) -> MatriboxController:
        """Abre automaticamente a conexão ao entrar em um bloco `with`."""
        self.connect()
        return self

    def __exit__(
        self,
        exception_type: type[BaseException] | None,
        exception_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Fecha automaticamente a conexão ao sair do bloco `with`."""
        self.disconnect()