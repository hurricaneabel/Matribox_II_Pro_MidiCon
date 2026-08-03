from matribox_core import MatriboxCore
from matribox_state import MatriboxState


class MatriboxController:
    def __init__(self, port_name):
        self.core = MatriboxCore(port_name)
        self.state = MatriboxState()

    # =====================
    # PRESETS E BANCOS
    # =====================

    def go_to_preset(self, bank, letter):
        self.core.go_to_preset(bank, letter)
        self.state.set_preset(bank, letter)

    def select_a(self):
        self.go_to_preset(self.state.bank, "A")

    def select_b(self):
        self.go_to_preset(self.state.bank, "B")

    def select_c(self):
        self.go_to_preset(self.state.bank, "C")

    def select_d(self):
        self.go_to_preset(self.state.bank, "D")

    def next_bank(self):
        bank = self.state.bank + 1
        if bank > 60:
            bank = 1
        self.go_to_preset(bank, self.state.letter)

    def previous_bank(self):
        bank = self.state.bank - 1
        if bank < 1:
            bank = 60
        self.go_to_preset(bank, self.state.letter)

    # =====================
    # NAVEGAÇÃO NATIVA MIDI
    # =====================

    def bank_next(self):
        self.core.bank_next()

    def bank_previous(self):
        self.core.bank_previous()

    def preset_next(self):
        self.core.preset_next()

    def preset_previous(self):
        self.core.preset_previous()

    def bank_next_wait(self):
        self.core.bank_next_wait()

    def bank_previous_wait(self):
        self.core.bank_previous_wait()

    def bank_wait(self):
        self.core.bank_wait()

    # =====================
    # MODOS
    # =====================

    def set_stomp_mode(self):
        self.core.set_stomp_mode()
        self.state.set_mode("stomp")

    def set_preset_mode(self):
        self.core.set_preset_mode()
        self.state.set_mode("preset")

    # =====================
    # CTRLS
    # =====================

    def ctrl(self, number):
        self.core.ctrl(number)

    def ctrl1(self):
        self.core.ctrl1()

    def ctrl2(self):
        self.core.ctrl2()

    def ctrl3(self):
        self.core.ctrl3()

    def ctrl4(self):
        self.core.ctrl4()

    # =====================
    # MÓDULOS / BLOCOS
    # =====================

    def toggle_module(self, module_number):
        enabled = self.state.toggle_module(module_number)
        self.core.module_set(module_number, enabled)
        return enabled

    def module_on(self, module_number):
        self.state.set_module(module_number, True)
        self.core.module_on(module_number)

    def module_off(self, module_number):
        self.state.set_module(module_number, False)
        self.core.module_off(module_number)

    # =====================
    # TUNER
    # =====================

    def toggle_tuner(self):
        enabled = self.state.toggle_tuner()
        if enabled:
            self.core.tuner_on()
        else:
            self.core.tuner_off()
        return enabled

    def tuner_on(self):
        self.state.set_tuner(True)
        self.core.tuner_on()

    def tuner_off(self):
        self.state.set_tuner(False)
        self.core.tuner_off()

    # =====================
    # VOLUME / EXPRESSION
    # =====================

    def preset_volume(self, volume):
        self.state.set_preset_volume(volume)
        self.core.preset_volume(volume)

    def exp1(self, value):
        self.state.set_exp1(value)
        self.core.exp1(value)

    def exp1_a(self):
        self.state.set_exp1_mode("A")
        self.core.exp1_a()

    def exp1_b(self):
        self.state.set_exp1_mode("B")
        self.core.exp1_b()

    # =====================
    # QUICK ACCESS KNOBS
    # =====================

    def quick_knob(self, knob_number, value):
        self.state.set_quick_knob(knob_number, value)
        self.core.quick_knob(knob_number, value)

    def quick_knob_up(self, knob_number):
        self.state.quick_knob_up(knob_number)
        self.core.quick_knob_up(knob_number)

    def quick_knob_down(self, knob_number):
        self.state.quick_knob_down(knob_number)
        self.core.quick_knob_down(knob_number)

    # =====================
    # BPM / TEMPO
    # =====================

    def tap_tempo(self):
        self.core.tap_tempo()

    def tap_bpm(self, bpm, taps=4):
        self.state.set_bpm(bpm)
        self.core.tap_bpm(bpm, taps)

    def set_bpm(self, bpm):
        self.state.set_bpm(bpm)
        self.core.set_bpm(bpm)

    # =====================
    # LOOPER
    # =====================

    def looper_on(self):
        self.state.set_looper_enabled(True)
        self.core.looper_on()

    def looper_off(self):
        self.state.set_looper_enabled(False)
        self.core.looper_off()

    def looper_record(self):
        self.state.set_looper_recording(True)
        self.core.looper_record()

    def looper_auto_record(self):
        self.state.set_looper_recording(True)
        self.core.looper_auto_record()

    def looper_play(self):
        self.state.set_looper_playing(True)
        self.core.looper_play()

    def looper_stop(self):
        self.state.set_looper_playing(False)
        self.state.set_looper_recording(False)
        self.core.looper_stop()

    def looper_undo_redo(self):
        self.core.looper_undo_redo()

    def looper_delete(self):
        self.state.set_looper_playing(False)
        self.state.set_looper_recording(False)
        self.core.looper_delete()

    def looper_record_volume(self, volume):
        self.state.set_looper_record_volume(volume)
        self.core.looper_record_volume(volume)

    def looper_playback_volume(self, volume):
        self.state.set_looper_playback_volume(volume)
        self.core.looper_playback_volume(volume)

    def looper_pre(self):
        self.state.set_looper_position("pre")
        self.core.looper_pre()

    def looper_post(self):
        self.state.set_looper_position("post")
        self.core.looper_post()

    # =====================
    # DRUM MACHINE
    # =====================

    def drum_menu_on(self):
        self.state.set_drum_menu(True)
        self.core.drum_menu_on()

    def drum_menu_off(self):
        self.state.set_drum_menu(False)
        self.core.drum_menu_off()

    def drum_play(self):
        self.state.set_drum_playing(True)
        self.core.drum_play()

    def drum_stop(self):
        self.state.set_drum_playing(False)
        self.core.drum_stop()

    def drum_rhythm(self, rhythm):
        self.state.set_drum_rhythm(rhythm)
        self.core.drum_rhythm(rhythm)

    def drum_volume(self, volume):
        self.state.set_drum_volume(volume)
        self.core.drum_volume(volume)

    # =====================
    # UTILIDADES
    # =====================

    def close(self):
        self.core.close()