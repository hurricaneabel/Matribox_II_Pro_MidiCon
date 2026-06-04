class MatriboxState:
    def __init__(self):
        # =====================
        # PRESET / BANCO
        # =====================

        self.bank = 1
        self.letter = "A"
        self.mode = "stomp"

        # =====================
        # MÓDULOS / BLOCOS
        # =====================
        # None = desconhecido
        # True = ligado
        # False = desligado

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

        # =====================
        # TUNER
        # =====================

        self.tuner = False

        # =====================
        # VOLUME / EXPRESSION
        # =====================

        self.preset_volume = None
        self.exp1_value = None
        self.exp1_mode = None  # "A", "B" ou None

        # =====================
        # QUICK ACCESS KNOBS
        # =====================

        self.quick_knobs = {
            1: None,
            2: None,
            3: None,
        }

        # =====================
        # BPM / TEMPO
        # =====================

        self.bpm = None

        # =====================
        # LOOPER
        # =====================

        self.looper_enabled = False
        self.looper_playing = False
        self.looper_recording = False
        self.looper_record_volume = None
        self.looper_playback_volume = None
        self.looper_position = None  # "pre", "post" ou None

        # =====================
        # DRUM MACHINE
        # =====================

        self.drum_menu = False
        self.drum_playing = False
        self.drum_rhythm = None
        self.drum_volume = None

    # =====================
    # PROPRIEDADES
    # =====================

    @property
    def preset_name(self):
        return f"{self.bank:02d}{self.letter}"

    # =====================
    # PRESET / BANCO
    # =====================

    def set_preset(self, bank, letter):
        self.bank = int(bank)
        self.letter = letter.upper()

    def set_mode(self, mode):
        mode = mode.lower()

        if mode not in ["stomp", "preset"]:
            raise ValueError("Modo precisa ser 'stomp' ou 'preset'.")

        self.mode = mode

    # =====================
    # MÓDULOS / BLOCOS
    # =====================

    def toggle_module(self, module_number):
        if module_number not in self.modules:
            raise ValueError("Módulo precisa estar entre 1 e 12.")

        current = self.modules[module_number]

        if current is None:
            self.modules[module_number] = True
        else:
            self.modules[module_number] = not current

        return self.modules[module_number]

    def set_module(self, module_number, enabled):
        if module_number not in self.modules:
            raise ValueError("Módulo precisa estar entre 1 e 12.")

        self.modules[module_number] = bool(enabled)

    # =====================
    # TUNER
    # =====================

    def toggle_tuner(self):
        self.tuner = not self.tuner
        return self.tuner

    def set_tuner(self, enabled):
        self.tuner = bool(enabled)

    # =====================
    # VOLUME / EXPRESSION
    # =====================

    def set_preset_volume(self, volume):
        self.preset_volume = max(0, min(100, int(volume)))

    def set_exp1(self, value):
        self.exp1_value = max(0, min(100, int(value)))

    def set_exp1_mode(self, mode):
        mode = mode.upper()

        if mode not in ["A", "B"]:
            raise ValueError("EXP1 precisa ser 'A' ou 'B'.")

        self.exp1_mode = mode

    # =====================
    # QUICK ACCESS KNOBS
    # =====================

    def set_quick_knob(self, knob_number, value):
        if knob_number not in self.quick_knobs:
            raise ValueError("Quick Knob precisa ser 1, 2 ou 3.")

        self.quick_knobs[knob_number] = max(0, min(100, int(value)))

    def quick_knob_up(self, knob_number):
        if knob_number not in self.quick_knobs:
            raise ValueError("Quick Knob precisa ser 1, 2 ou 3.")

        current = self.quick_knobs[knob_number]

        if current is None:
            self.quick_knobs[knob_number] = None
        else:
            self.quick_knobs[knob_number] = min(100, current + 1)

    def quick_knob_down(self, knob_number):
        if knob_number not in self.quick_knobs:
            raise ValueError("Quick Knob precisa ser 1, 2 ou 3.")

        current = self.quick_knobs[knob_number]

        if current is None:
            self.quick_knobs[knob_number] = None
        else:
            self.quick_knobs[knob_number] = max(0, current - 1)

    # =====================
    # BPM / TEMPO
    # =====================

    def set_bpm(self, bpm):
        bpm = int(bpm)

        if bpm < 40 or bpm > 300:
            raise ValueError("BPM deve estar entre 40 e 300.")

        self.bpm = bpm

    # =====================
    # LOOPER
    # =====================

    def set_looper_enabled(self, enabled):
        self.looper_enabled = bool(enabled)

        if not self.looper_enabled:
            self.looper_playing = False
            self.looper_recording = False

    def set_looper_playing(self, enabled):
        self.looper_playing = bool(enabled)

        if self.looper_playing:
            self.looper_recording = False

    def set_looper_recording(self, enabled):
        self.looper_recording = bool(enabled)

        if self.looper_recording:
            self.looper_playing = False

    def set_looper_record_volume(self, volume):
        self.looper_record_volume = max(0, min(100, int(volume)))

    def set_looper_playback_volume(self, volume):
        self.looper_playback_volume = max(0, min(100, int(volume)))

    def set_looper_position(self, position):
        position = position.lower()

        if position not in ["pre", "post"]:
            raise ValueError("Looper position precisa ser 'pre' ou 'post'.")

        self.looper_position = position

    # =====================
    # DRUM MACHINE
    # =====================

    def set_drum_menu(self, enabled):
        self.drum_menu = bool(enabled)

    def set_drum_playing(self, enabled):
        self.drum_playing = bool(enabled)

    def set_drum_rhythm(self, rhythm):
        self.drum_rhythm = max(0, min(99, int(rhythm)))

    def set_drum_volume(self, volume):
        self.drum_volume = max(0, min(100, int(volume)))