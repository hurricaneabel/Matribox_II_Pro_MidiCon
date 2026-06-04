class MatriboxState:
    def __init__(self):
        self.bank = 1
        self.letter = "A"
        self.mode = "stomp"
        self.tuner = False

        self.modules = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
            10: None,
            11: None,
            12: None,
        }

    @property
    def preset_name(self):
        return f"{self.bank:02d}{self.letter}"

    def set_preset(self, bank, letter):
        self.bank = int(bank)
        self.letter = letter.upper()

    def toggle_module(self, module_number):
        self.modules[module_number] = not self.modules[module_number]
        return self.modules[module_number]

    def set_module(self, module_number, enabled):
        self.modules[module_number] = bool(enabled)

    def toggle_tuner(self):
        self.tuner = not self.tuner
        return self.tuner