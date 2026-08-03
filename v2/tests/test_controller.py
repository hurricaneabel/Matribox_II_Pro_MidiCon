"""
Testes automáticos do controlador da Matribox II Pro.

Estes testes não abrem uma porta MIDI real. Um objeto simulado registra os
comandos que o controlador tentaria enviar à pedaleira.
"""

from __future__ import annotations

import unittest
from unittest.mock import Mock, call

from matribox_midi.commands import ControlChange, EffectModule, LooperPlacementValue, OperatingModeValue, SwitchValue
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


class TestValueRanges(unittest.TestCase):
    """Testa os limites de volume e expressão."""

    def setUp(self) -> None:
        """Cria um controlador com saída MIDI simulada."""
        self.controller = MatriboxController()
        self.midi_output = Mock()
        self.controller._midi_output = self.midi_output

    def test_accepts_maximum_preset_volume(self) -> None:
        """Aceita o volume máximo permitido pelo manual."""
        self.controller.set_preset_volume(100)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.PRESET_VOLUME,
            100,
        )

    def test_rejects_preset_volume_above_100(self) -> None:
        """Rejeita volume acima do limite permitido."""
        with self.assertRaises(ValueError):
            self.controller.set_preset_volume(101)

    def test_accepts_maximum_expression_value(self) -> None:
        """Aceita o valor máximo de expressão."""
        self.controller.set_expression(100)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.EXPRESSION,
            100,
        )

    def test_rejects_expression_value_above_100(self) -> None:
        """Rejeita expressão acima do limite permitido."""
        with self.assertRaises(ValueError):
            self.controller.set_expression(101) 

class TestQuickAccessKnobs(unittest.TestCase):
    """Testa os três knobs Quick Access."""

    def setUp(self) -> None:
        """Cria um controlador com saída MIDI simulada."""
        self.controller = MatriboxController()
        self.midi_output = Mock()
        self.controller._midi_output = self.midi_output

    def test_sets_knob_1_value(self) -> None:
        """Confirma o valor absoluto do knob 1 pelo CC 16."""
        self.controller.set_quick_access_knob(1, 50)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.QUICK_ACCESS_KNOB_1_VALUE,
            50,
        )

    def test_sets_knob_2_value(self) -> None:
        """Confirma o valor absoluto do knob 2 pelo CC 18."""
        self.controller.set_quick_access_knob(2, 40)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.QUICK_ACCESS_KNOB_2_VALUE,
            40,
        )

    def test_sets_knob_3_value(self) -> None:
        """Confirma o valor absoluto do knob 3 pelo CC 20."""
        self.controller.set_quick_access_knob(3, 30)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.QUICK_ACCESS_KNOB_3_VALUE,
            30,
        )

    def test_increases_knob_2(self) -> None:
        """Usa o CC 19 com valor 127 para aumentar um passo."""
        self.controller.increase_quick_access_knob(2)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.QUICK_ACCESS_KNOB_2_STEP,
            127,
        )

    def test_decreases_knob_3(self) -> None:
        """Usa o CC 21 com valor 0 para diminuir um passo."""
        self.controller.decrease_quick_access_knob(3)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.QUICK_ACCESS_KNOB_3_STEP,
            0,
        )

    def test_rejects_invalid_knob(self) -> None:
        """Rejeita números de knobs diferentes de 1, 2 ou 3."""
        with self.assertRaises(ValueError):
            self.controller.set_quick_access_knob(4, 50)

    def test_rejects_value_above_100(self) -> None:
        """Rejeita valores absolutos acima de 100."""
        with self.assertRaises(ValueError):
            self.controller.set_quick_access_knob(1, 101)

class TestTempo(unittest.TestCase):
    """Testa a conversão do BPM para os CC 68 e 69."""

    def setUp(self) -> None:
        """Cria um controlador com saída MIDI simulada."""
        self.controller = MatriboxController()
        self.midi_output = Mock()
        self.controller._midi_output = self.midi_output

    def test_sets_120_bpm(self) -> None:
        """Converte 120 BPM em MSB 0 e LSB 120."""
        self.controller.set_bpm(120)

        self.midi_output.send_control_change.assert_has_calls(
            [
                call(ControlChange.PRESET_BPM_MSB, 0),
                call(ControlChange.PRESET_BPM_LSB, 120),
            ]
        )

    def test_sets_200_bpm(self) -> None:
        """Converte 200 BPM em MSB 1 e LSB 72."""
        self.controller.set_bpm(200)

        self.midi_output.send_control_change.assert_has_calls(
            [
                call(ControlChange.PRESET_BPM_MSB, 1),
                call(ControlChange.PRESET_BPM_LSB, 72),
            ]
        )

    def test_rejects_bpm_below_40(self) -> None:
        """Rejeita BPM abaixo do limite mínimo."""
        with self.assertRaises(ValueError):
            self.controller.set_bpm(39)

    def test_rejects_bpm_above_300(self) -> None:
        """Rejeita BPM acima do limite máximo."""
        with self.assertRaises(ValueError):
            self.controller.set_bpm(301)

class TestModesEffectsAndTuner(unittest.TestCase):
    """Testa modos de operação, módulos de efeito e afinador."""

    def setUp(self) -> None:
        """Cria um controlador com saída MIDI simulada."""
        self.controller = MatriboxController()
        self.midi_output = Mock()
        self.controller._midi_output = self.midi_output

    def test_activates_preset_mode(self) -> None:
        """Ativa o modo Preset."""
        self.controller.preset_mode()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.PRESET_STOMP_MODE,
            OperatingModeValue.PRESET,
        )

    def test_activates_stomp_mode(self) -> None:
        """Ativa o modo Stomp."""
        self.controller.stomp_mode()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.PRESET_STOMP_MODE,
            OperatingModeValue.STOMP,
        )

    def test_activates_effect_module_1(self) -> None:
        """Ativa o primeiro módulo de efeito."""
        self.controller.effect_module_on(EffectModule.MODULE_1)

        self.midi_output.send_control_change.assert_called_once_with(
            EffectModule.MODULE_1,
            SwitchValue.ON,
        )

    def test_deactivates_effect_module_12(self) -> None:
        """Desativa o último módulo de efeito."""
        self.controller.effect_module_off(EffectModule.MODULE_12)

        self.midi_output.send_control_change.assert_called_once_with(
            EffectModule.MODULE_12,
            SwitchValue.OFF,
        )

    def test_activates_tuner(self) -> None:
        """Ativa o afinador."""
        self.controller.tuner_on()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.TUNER,
            SwitchValue.ON,
        )

    def test_deactivates_tuner(self) -> None:
        """Desativa o afinador."""
        self.controller.tuner_off()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.TUNER,
            SwitchValue.OFF,
        )

class TestLooperControls(unittest.TestCase):
    """Testa os principais controles e limites do Looper."""

    def setUp(self) -> None:
        """Cria um controlador com saída MIDI simulada."""
        self.controller = MatriboxController()
        self.midi_output = Mock()
        self.controller._midi_output = self.midi_output

    def test_activates_looper(self) -> None:
        """Abre e ativa o menu do Looper."""
        self.controller.looper_on()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.LOOPER,
            SwitchValue.ON,
        )

    def test_deactivates_looper(self) -> None:
        """Fecha e desativa o menu do Looper."""
        self.controller.looper_off()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.LOOPER,
            SwitchValue.OFF,
        )

    def test_executes_undo_redo(self) -> None:
        """Envia o comando de undo ou redo."""
        self.controller.looper_undo_redo()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.LOOPER_UNDO_REDO,
            SwitchValue.ON,
        )

    def test_sets_recording_volume(self) -> None:
        """Define o volume de gravação do Looper."""
        self.controller.set_looper_recording_volume(60)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.LOOPER_RECORDING_VOLUME,
            60,
        )

    def test_rejects_invalid_recording_volume(self) -> None:
        """Rejeita volume de gravação acima de 100."""
        with self.assertRaises(ValueError):
            self.controller.set_looper_recording_volume(101)

    def test_sets_playback_volume(self) -> None:
        """Define o volume de reprodução do Looper."""
        self.controller.set_looper_playback_volume(70)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.LOOPER_PLAYBACK_VOLUME,
            70,
        )

    def test_selects_pre_placement(self) -> None:
        """Posiciona o Looper antes dos efeitos."""
        self.controller.set_looper_pre()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.LOOPER_PLACEMENT,
            LooperPlacementValue.PRE,
        )

    def test_selects_post_placement(self) -> None:
        """Posiciona o Looper depois dos efeitos."""
        self.controller.set_looper_post()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.LOOPER_PLACEMENT,
            LooperPlacementValue.POST,
        )

class TestDrumControls(unittest.TestCase):
    """Testa os controles da bateria eletrônica."""

    def setUp(self) -> None:
        """Cria um controlador com saída MIDI simulada."""
        self.controller = MatriboxController()
        self.midi_output = Mock()
        self.controller._midi_output = self.midi_output

    def test_opens_drum_menu(self) -> None:
        """Abre o menu da bateria."""
        self.controller.drum_menu_on()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.DRUM_MENU,
            SwitchValue.ON,
        )

    def test_closes_drum_menu(self) -> None:
        """Fecha o menu da bateria."""
        self.controller.drum_menu_off()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.DRUM_MENU,
            SwitchValue.OFF,
        )

    def test_starts_drum_playback(self) -> None:
        """Inicia a reprodução da bateria."""
        self.controller.drum_play()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.DRUM_PLAY_STOP,
            SwitchValue.ON,
        )

    def test_stops_drum_playback(self) -> None:
        """Interrompe a reprodução da bateria."""
        self.controller.drum_stop()

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.DRUM_PLAY_STOP,
            SwitchValue.OFF,
        )

    def test_sets_drum_rhythm(self) -> None:
        """Seleciona um ritmo entre 0 e 99."""
        self.controller.set_drum_rhythm(50)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.DRUM_RHYTHM,
            50,
        )

    def test_rejects_invalid_drum_rhythm(self) -> None:
        """Rejeita ritmos acima de 99."""
        with self.assertRaises(ValueError):
            self.controller.set_drum_rhythm(100)

    def test_sets_drum_volume(self) -> None:
        """Define o volume da bateria."""
        self.controller.set_drum_volume(70)

        self.midi_output.send_control_change.assert_called_once_with(
            ControlChange.DRUM_VOLUME,
            70,
        )

    def test_rejects_invalid_drum_volume(self) -> None:
        """Rejeita volume acima de 100."""
        with self.assertRaises(ValueError):
            self.controller.set_drum_volume(101)

if __name__ == "__main__":
    unittest.main()