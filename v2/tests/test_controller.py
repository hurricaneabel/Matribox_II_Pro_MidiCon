"""
Testes automáticos do controlador da Matribox II Pro.

Estes testes não abrem uma porta MIDI real. Um objeto simulado registra os
comandos que o controlador tentaria enviar à pedaleira.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock

from matribox_midi.commands import ControlChange
from matribox_midi.controller import MatriboxController


class TestPresetSelection(unittest.TestCase):
    """Testa a conversão de banco e letra para comandos MIDI."""

    def setUp(self) -> None:
        """Cria um controlador com uma saída MIDI simulada."""
        self.controller = MatriboxController()
        self.midi_output = Mock()
        self.controller._midi_output = self.midi_output

    def test_selects_first_preset(self) -> None:
        """Confirma a conversão de 01A."""
        self.controller.select_preset(1, "A")

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.BANK_SELECT,
            0,
        )
        self.midi_output.send_program_change.assert_called_once_with(0)

    def test_selects_last_preset_of_first_group(self) -> None:
        """Confirma a conversão de 30D."""
        self.controller.select_preset(30, "D")

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.BANK_SELECT,
            0,
        )
        self.midi_output.send_program_change.assert_called_once_with(119)

    def test_selects_first_preset_of_second_group(self) -> None:
        """Confirma a conversão de 31A."""
        self.controller.select_preset(31, "A")

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.BANK_SELECT,
            1,
        )
        self.midi_output.send_program_change.assert_called_once_with(0)

    def test_selects_last_available_preset(self) -> None:
        """Confirma a conversão de 60D."""
        self.controller.select_preset(60, "D")

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.BANK_SELECT,
            1,
        )
        self.midi_output.send_program_change.assert_called_once_with(119)

    def test_rejects_invalid_bank(self) -> None:
        """Impede bancos fora do intervalo de 1 a 60."""
        with self.assertRaises(ValueError):
            self.controller.select_preset(61, "A")

    def test_rejects_invalid_preset_letter(self) -> None:
        """Impede letras diferentes de A, B, C ou D."""
        with self.assertRaises(ValueError):
            self.controller.select_preset(1, "E")


if __name__ == "__main__":
    unittest.main()