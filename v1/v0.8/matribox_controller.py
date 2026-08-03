from matribox_core import MatriboxCore
from matribox_state import MatriboxState


class MatriboxController:
    def __init__(self, port_name):
        self.core = MatriboxCore(port_name)
        self.state = MatriboxState()

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

    def set_stomp_mode(self):
        self.core.set_stomp_mode()
        self.state.mode = "stomp"

    def set_preset_mode(self):
        self.core.set_preset_mode()
        self.state.mode = "preset"

    def ctrl(self, number):
        self.core.ctrl(number)

    def toggle_module(self, module_number):
        enabled = self.state.toggle_module(module_number)
        self.core.module_set(module_number, enabled)
        return enabled

    def toggle_tuner(self):
        enabled = self.state.toggle_tuner()
        if enabled:
            self.core.tuner_on()
        else:
            self.core.tuner_off()
        return enabled

    def set_bpm(self, bpm):
        self.core.set_bpm(bpm)

    def close(self):
        self.core.close()