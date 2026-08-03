"""
Controle de alto nível da Matribox II Pro.

Este módulo oferece métodos com nomes claros, como ligar e desligar o
afinador, sem exigir que o usuário da biblioteca conheça números de
Control Change ou valores MIDI.
"""

from __future__ import annotations

from types import TracebackType

from .commands import ControlChange, EffectModule, SwitchValue
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