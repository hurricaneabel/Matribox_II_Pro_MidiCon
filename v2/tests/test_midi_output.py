"""
Testes automáticos da saída MIDI da Matribox II Pro.

Nenhuma porta MIDI real é aberta. As conexões e mensagens são simuladas.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

from matribox_midi.midi_output import MatriboxMidiOutput


class TestMidiConnection(unittest.TestCase):
    """Testa a abertura e o fechamento da conexão MIDI."""

    @patch("matribox_midi.midi_output.mido.open_output")
    def test_connects_to_requested_port(self, open_output: Mock) -> None:
        """Abre a porta informada diretamente pelo usuário."""
        fake_port = Mock()
        open_output.return_value = fake_port

        midi_output = MatriboxMidiOutput("Porta de teste")
        result = midi_output.connect()

        open_output.assert_called_once_with("Porta de teste")
        self.assertEqual(result, "Porta de teste")
        self.assertTrue(midi_output.is_connected)
        self.assertEqual(midi_output.port_name, "Porta de teste")

    @patch(
        "matribox_midi.midi_output.find_matribox_output",
        return_value=None,
    )
    def test_rejects_connection_when_port_is_missing(
        self,
        find_output: Mock,
    ) -> None:
        """Informa erro quando nenhuma porta da Matribox é encontrada."""
        midi_output = MatriboxMidiOutput()

        with self.assertRaises(RuntimeError):
            midi_output.connect()

        find_output.assert_called_once_with()
        self.assertFalse(midi_output.is_connected)

    def test_disconnects_open_port(self) -> None:
        """Fecha a porta e limpa os dados da conexão."""
        fake_port = Mock()

        midi_output = MatriboxMidiOutput()
        midi_output._port = fake_port
        midi_output._active_port_name = "Porta de teste"

        midi_output.disconnect()

        fake_port.close.assert_called_once_with()
        self.assertFalse(midi_output.is_connected)
        self.assertIsNone(midi_output.port_name)


class TestMidiMessages(unittest.TestCase):
    """Testa a criação e o envio das mensagens MIDI."""

    def setUp(self) -> None:
        """Cria uma saída MIDI com uma porta simulada."""
        self.midi_output = MatriboxMidiOutput()
        self.fake_port = Mock()
        self.midi_output._port = self.fake_port

    def test_sends_control_change(self) -> None:
        """Envia um Control Change com os valores informados."""
        self.midi_output.send_control_change(
            control=58,
            value=127,
            channel=0,
        )

        message = self.fake_port.send.call_args.args[0]

        self.assertEqual(message.type, "control_change")
        self.assertEqual(message.control, 58)
        self.assertEqual(message.value, 127)
        self.assertEqual(message.channel, 0)

    def test_rejects_control_change_without_connection(self) -> None:
        """Impede o envio quando nenhuma porta está aberta."""
        midi_output = MatriboxMidiOutput()

        with self.assertRaises(RuntimeError):
            midi_output.send_control_change(58, 127)

    def test_rejects_invalid_control_change_arguments(self) -> None:
        """Rejeita controle, valor e canal fora dos limites MIDI."""
        invalid_arguments = [
            {"control": 128, "value": 0, "channel": 0},
            {"control": 0, "value": 128, "channel": 0},
            {"control": 0, "value": 0, "channel": 16},
        ]

        for arguments in invalid_arguments:
            with self.subTest(arguments=arguments):
                with self.assertRaises(ValueError):
                    self.midi_output.send_control_change(**arguments)

    def test_sends_program_change(self) -> None:
        """Envia um Program Change com o programa informado."""
        self.midi_output.send_program_change(
            program=119,
            channel=0,
        )

        message = self.fake_port.send.call_args.args[0]

        self.assertEqual(message.type, "program_change")
        self.assertEqual(message.program, 119)
        self.assertEqual(message.channel, 0)

    def test_rejects_invalid_program_change(self) -> None:
        """Rejeita programa e canal fora dos limites MIDI."""
        with self.assertRaises(ValueError):
            self.midi_output.send_program_change(128)

        with self.assertRaises(ValueError):
            self.midi_output.send_program_change(0, channel=16)


if __name__ == "__main__":
    unittest.main()