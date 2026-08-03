import time
import mido


class MatriboxCore:
    LETTERS = ["A", "B", "C", "D"]

    def __init__(self, port_name, midi_channel=0):
        self.port_name = port_name
        self.midi_channel = midi_channel
        self.out = mido.open_output(port_name)

        self.mode = "stomp"
        self.bank = 1
        self.letter = "A"

    # =====================
    # MIDI BASE
    # =====================

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
        pc = max(1, min(120, int(pc)))
        self.out.send(
            mido.Message(
                "program_change",
                channel=self.midi_channel,
                program=pc - 1,
            )
        )

    # =====================
    # PRESETS E BANCOS
    # =====================

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

        print(
            f"Preset selecionado: {self.bank:02d}{self.letter} "
            f"| CC0={bank_msb}, PC={pc}"
        )

    def next_bank(self):
        self.bank = self.bank + 1 if self.bank < 60 else 1
        self.go_to_preset(self.bank, self.letter)

    def previous_bank(self):
        self.bank = self.bank - 1 if self.bank > 1 else 60
        self.go_to_preset(self.bank, self.letter)

    def select_a(self):
        self.go_to_preset(self.bank, "A")

    def select_b(self):
        self.go_to_preset(self.bank, "B")

    def select_c(self):
        self.go_to_preset(self.bank, "C")

    def select_d(self):
        self.go_to_preset(self.bank, "D")

    # =====================
    # NAVEGAÇÃO NATIVA MIDI
    # =====================

    def bank_next(self):
        self.send_cc(22, 127)

    def bank_previous(self):
        self.send_cc(23, 127)

    def preset_next(self):
        self.send_cc(24, 127)

    def preset_previous(self):
        self.send_cc(25, 127)

    def bank_next_wait(self):
        self.send_cc(26, 127)

    def bank_previous_wait(self):
        self.send_cc(27, 127)

    def bank_wait(self):
        self.send_cc(28, 127)

    # =====================
    # MODOS
    # =====================

    def set_stomp_mode(self):
        self.send_cc(29, 0)
        self.mode = "stomp"
        print("Modo: STOMP")

    def set_preset_mode(self):
        self.send_cc(29, 64)
        self.mode = "preset"
        print("Modo: PRESET")

    # =====================
    # CTRLS
    # =====================

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

    # =====================
    # MÓDULOS / BLOCOS
    # =====================

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

    # =====================
    # TUNER
    # =====================

    def tuner_on(self):
        self.send_cc(58, 127)

    def tuner_off(self):
        self.send_cc(58, 0)

    # =====================
    # VOLUME / EXPRESSION
    # =====================

    def preset_volume(self, volume):
        volume = max(0, min(100, int(volume)))
        self.send_cc(7, volume)

    def exp1(self, value):
        value = max(0, min(100, int(value)))
        self.send_cc(11, value)

    def exp1_a(self):
        self.send_cc(13, 0)

    def exp1_b(self):
        self.send_cc(13, 127)

    # =====================
    # QUICK ACCESS KNOBS
    # =====================

    def quick_knob(self, knob_number, value):
        if knob_number not in [1, 2, 3]:
            raise ValueError("Quick Knob precisa ser 1, 2 ou 3.")

        value = max(0, min(100, int(value)))

        cc_map = {
            1: 16,
            2: 18,
            3: 20,
        }

        self.send_cc(cc_map[knob_number], value)

    def quick_knob_down(self, knob_number):
        if knob_number not in [1, 2, 3]:
            raise ValueError("Quick Knob precisa ser 1, 2 ou 3.")

        cc_map = {
            1: 17,
            2: 19,
            3: 21,
        }

        self.send_cc(cc_map[knob_number], 0)

    def quick_knob_up(self, knob_number):
        if knob_number not in [1, 2, 3]:
            raise ValueError("Quick Knob precisa ser 1, 2 ou 3.")

        cc_map = {
            1: 17,
            2: 19,
            3: 21,
        }

        self.send_cc(cc_map[knob_number], 64)

    # =====================
    # BPM / TEMPO
    # =====================

    def tap_tempo(self):
        self.send_cc(70, 127)

    def tap_bpm(self, bpm, taps=4):
        bpm = int(bpm)

        if bpm <= 0:
            raise ValueError("BPM precisa ser maior que zero.")

        interval = 60 / bpm

        for _ in range(taps):
            self.tap_tempo()
            time.sleep(interval)

    def set_bpm(self, bpm):
        bpm = int(bpm)

        if bpm < 40 or bpm > 300:
            raise ValueError("BPM deve estar entre 40 e 300.")

        if bpm <= 127:
            self.send_cc(68, 0)
            self.send_cc(69, bpm)
        elif bpm <= 255:
            self.send_cc(68, 1)
            self.send_cc(69, bpm - 128)
        else:
            self.send_cc(68, 2)
            self.send_cc(69, bpm - 256)

        print(f"BPM definido para {bpm}")

    # =====================
    # LOOPER
    # =====================

    def looper_on(self):
        self.send_cc(59, 127)

    def looper_off(self):
        self.send_cc(59, 0)

    def looper_record(self):
        self.send_cc(60, 127)

    def looper_auto_record(self):
        self.send_cc(61, 127)

    def looper_play(self):
        self.send_cc(62, 127)

    def looper_stop(self):
        self.send_cc(62, 0)

    def looper_undo_redo(self):
        self.send_cc(63, 127)

    def looper_delete(self):
        self.send_cc(64, 127)

    def looper_record_volume(self, volume):
        volume = max(0, min(100, int(volume)))
        self.send_cc(65, volume)

    def looper_playback_volume(self, volume):
        volume = max(0, min(100, int(volume)))
        self.send_cc(66, volume)

    def looper_pre(self):
        self.send_cc(67, 127)

    def looper_post(self):
        self.send_cc(67, 0)

    # =====================
    # DRUM MACHINE
    # =====================

    def drum_menu_on(self):
        self.send_cc(92, 127)

    def drum_menu_off(self):
        self.send_cc(92, 0)

    def drum_play(self):
        self.send_cc(93, 127)

    def drum_stop(self):
        self.send_cc(93, 0)

    def drum_rhythm(self, rhythm):
        rhythm = max(0, min(99, int(rhythm)))
        self.send_cc(94, rhythm)

    def drum_volume(self, volume):
        volume = max(0, min(100, int(volume)))
        self.send_cc(95, volume)

    # =====================
    # UTILIDADES
    # =====================

    def close(self):
        self.out.close()