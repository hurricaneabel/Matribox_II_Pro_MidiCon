import mido


class MatriboxCore:
    LETTERS = ["A", "B", "C", "D"]

    def __init__(self, port_name, midi_channel=0):
        self.port_name = port_name
        self.midi_channel = midi_channel
        self.out = mido.open_output(port_name)

        self.mode = "preset"   # "preset" ou "stomp"
        self.bank = 1
        self.letter = "A"

    def send_cc(self, cc, value):
        value = max(0, min(127, int(value)))
        self.out.send(
            mido.Message(
                "control_change",
                channel=self.midi_channel,
                control=cc,
                value=value,
            )
        )

    def send_pc(self, pc):
        """
        O manual fala PC 1-120.
        A biblioteca mido envia program_change de 0-119.
        """
        pc = max(1, min(120, int(pc)))
        self.out.send(
            mido.Message(
                "program_change",
                channel=self.midi_channel,
                program=pc - 1,
            )
        )

    def calculate_bank_msb_and_pc(self, bank, letter):
        bank = int(bank)
        letter = letter.upper()

        if bank < 1 or bank > 60:
            raise ValueError("Banco precisa estar entre 1 e 60.")

        if letter not in self.LETTERS:
            raise ValueError("Letra precisa ser A, B, C ou D.")

        if bank <= 30:
            bank_msb = 0
            bank_inside_group = bank
        else:
            bank_msb = 1
            bank_inside_group = bank - 30

        letter_index = self.LETTERS.index(letter)

        pc = ((bank_inside_group - 1) * 4) + letter_index + 1

        return bank_msb, pc

    def go_to_preset(self, bank, letter):
        bank_msb, pc = self.calculate_bank_msb_and_pc(bank, letter)

        self.send_cc(0, bank_msb)
        self.send_pc(pc)

        self.bank = int(bank)
        self.letter = letter.upper()

        print(f"Preset selecionado: {self.bank:02d}{self.letter} | CC0={bank_msb}, PC={pc}")

    def next_bank(self):
        if self.bank < 60:
            self.bank += 1
        else:
            self.bank = 1

        self.go_to_preset(self.bank, self.letter)

    def previous_bank(self):
        if self.bank > 1:
            self.bank -= 1
        else:
            self.bank = 60

        self.go_to_preset(self.bank, self.letter)

    def select_a(self):
        self.go_to_preset(self.bank, "A")

    def select_b(self):
        self.go_to_preset(self.bank, "B")

    def select_c(self):
        self.go_to_preset(self.bank, "C")

    def select_d(self):
        self.go_to_preset(self.bank, "D")

    def set_stomp_mode(self):
        self.send_cc(29, 0)
        self.mode = "Stomp"
        print("Modo: STOMP")

    def set_preset_mode(self):
        self.send_cc(29, 64)
        self.mode = "Preset"
        print("Modo: PRESET")

    def tuner_on(self):
        self.send_cc(58, 127)

    def tuner_off(self):
        self.send_cc(58, 0)

    def close(self):
        self.out.close()

    def ctrl(self, number):
        if number not in [1, 2, 3, 4]:
            raise ValueError("CTRL precisa ser 1, 2, 3 ou 4.")

        cc = 70 + number
        self.send_cc(cc, 127)
        print(f"CTRL{number} enviado | CC{cc}")

    def ctrl1(self):
        self.ctrl(1)

    def ctrl2(self):
        self.ctrl(2)

    def ctrl3(self):
        self.ctrl(3)

    def ctrl4(self):
        self.ctrl(4)

    def module_on(self, module_number):
        if module_number < 1 or module_number > 12:
            raise ValueError("Módulo precisa estar entre 1 e 12.")

        cc = 42 + module_number
        self.send_cc(cc, 127)
        print(f"Módulo {module_number} ON | CC{cc}")

    def module_off(self, module_number):
        if module_number < 1 or module_number > 12:
            raise ValueError("Módulo precisa estar entre 1 e 12.")

        cc = 42 + module_number
        self.send_cc(cc, 0)
        print(f"Módulo {module_number} OFF | CC{cc}")

    def module_set(self, module_number, enabled):
        if enabled:
            self.module_on(module_number)
        else:
            self.module_off(module_number)

    def close(self):
        self.out.close()