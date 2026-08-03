"""
Gerenciamento da conexão MIDI de saída com a Matribox II Pro.

Este módulo possui responsabilidades específicas:

1. localizar a porta MIDI da pedaleira;
2. abrir a conexão;
3. manter a conexão disponível;
4. enviar mensagens MIDI básicas;
5. fechar a conexão corretamente.
"""

from __future__ import annotations

from types import TracebackType

import mido
from mido.ports import BaseOutput

from .ports import find_matribox_output


class MatriboxMidiOutput:
    """
    Representa uma conexão MIDI de saída com a Matribox II Pro.

    A classe pode localizar automaticamente a porta da pedaleira ou utilizar
    um nome de porta informado manualmente.
    """

    def __init__(self, port_name: str | None = None) -> None:
        """
        Inicializa o gerenciador da saída MIDI.

        Args:
            port_name:
                Nome completo da porta MIDI que deverá ser utilizada.

                Quando nenhum nome é informado, a classe procura
                automaticamente uma porta contendo "Matribox II Pro".
        """
        self._requested_port_name = port_name
        self._active_port_name: str | None = None
        self._port: BaseOutput | None = None

    @property
    def is_connected(self) -> bool:
        """
        Informa se existe uma conexão MIDI aberta.

        Returns:
            True quando a conexão está aberta.
            False quando não há conexão.
        """
        return self._port is not None

    @property
    def port_name(self) -> str | None:
        """
        Retorna o nome da porta atualmente conectada.

        Returns:
            Nome completo da porta ou None quando não existe conexão.
        """
        return self._active_port_name

    def connect(self) -> str:
        """
        Localiza e abre a porta MIDI da Matribox II Pro.

        Se a conexão já estiver aberta, o método retorna o nome da porta
        atual sem tentar abri-la novamente.

        Returns:
            Nome completo da porta MIDI aberta.

        Raises:
            RuntimeError:
                Quando nenhuma porta correspondente à Matribox é encontrada.
        """
        if self.is_connected and self._active_port_name is not None:
            return self._active_port_name

        port_name = self._requested_port_name or find_matribox_output()

        if port_name is None:
            raise RuntimeError(
                "A porta MIDI da Matribox II Pro não foi encontrada. "
                "Verifique se a pedaleira está ligada e conectada por USB."
            )

        self._port = mido.open_output(port_name)
        self._active_port_name = port_name

        return port_name

    def disconnect(self) -> None:
        """
        Fecha a conexão MIDI, caso ela esteja aberta.

        Chamar este método mais de uma vez é seguro. Quando não existe
        conexão, ele simplesmente não realiza nenhuma ação.
        """
        if self._port is None:
            return

        self._port.close()
        self._port = None
        self._active_port_name = None

    def send_control_change(
        self,
        control: int,
        value: int,
        channel: int = 0,
    ) -> None:
        """
        Envia uma mensagem MIDI do tipo Control Change.

        Args:
            control:
                Número do controle MIDI, entre 0 e 127.

            value:
                Valor enviado ao controle, entre 0 e 127.

            channel:
                Canal utilizado internamente pelo Mido, entre 0 e 15.
                O canal 0 do Mido corresponde ao canal MIDI 1.

        Raises:
            RuntimeError:
                Quando não existe uma conexão MIDI aberta.

            ValueError:
                Quando algum argumento está fora do intervalo permitido.
        """
        if self._port is None:
            raise RuntimeError(
                "Não existe uma conexão MIDI aberta. "
                "Execute connect() antes de enviar comandos."
            )

        if not 0 <= control <= 127:
            raise ValueError(
                "O número do controle deve estar entre 0 e 127."
            )

        if not 0 <= value <= 127:
            raise ValueError(
                "O valor do controle deve estar entre 0 e 127."
            )

        if not 0 <= channel <= 15:
            raise ValueError(
                "O canal MIDI deve estar entre 0 e 15."
            )

        message = mido.Message(
            "control_change",
            channel=channel,
            control=control,
            value=value,
        )

        self._port.send(message)

    def send_program_change(
        self,
        program: int,
        channel: int = 0,
    ) -> None:
        """
        Envia uma mensagem MIDI do tipo Program Change.

        Program Change é utilizado para selecionar presets ou programas
        armazenados no equipamento MIDI.

        Args:
            program:
                Número do programa MIDI, entre 0 e 127.

            channel:
                Canal utilizado internamente pelo Mido, entre 0 e 15.
                O canal 0 do Mido corresponde ao canal MIDI 1.

        Raises:
            RuntimeError:
                Quando não existe uma conexão MIDI aberta.

            ValueError:
                Quando algum argumento está fora do intervalo permitido.
        """
        if self._port is None:
            raise RuntimeError(
                "Não existe uma conexão MIDI aberta. "
                "Execute connect() antes de enviar comandos."
            )

        if not 0 <= program <= 127:
            raise ValueError(
                "O número do programa deve estar entre 0 e 127."
            )

        if not 0 <= channel <= 15:
            raise ValueError(
                "O canal MIDI deve estar entre 0 e 15."
            )

        message = mido.Message(
            "program_change",
            channel=channel,
            program=program,
        )

        self._port.send(message)

    def __enter__(self) -> MatriboxMidiOutput:
        """
        Abre automaticamente a conexão ao entrar em um bloco `with`.

        Exemplo:
            with MatriboxMidiOutput() as midi_output:
                print(midi_output.port_name)
        """
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