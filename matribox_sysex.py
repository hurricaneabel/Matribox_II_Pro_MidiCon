LETTERS = ["A", "B", "C", "D"]


DYN_EFFECTS = {
    (0, 0): "COMP1",
    (0, 1): "COMP2",
    (0, 3): "COMP3",

    (1, 4): "M-Boost",
    (1, 10): "E-Boost",
    (0, 10): "AC-Boost",

    (0, 11): "BB-Boost",
    (0, 12): "RC-Boost",

    (1, 9): "FAT-Boost",

    (1, 11): "Gate 1",
    (1, 13): "Gate 2",
    (2, 1): "Gate 3",
}
FREQ_EFFECTS = {
    (1, 9): "FILTER",
    (2, 1): "OCTAVER",
    (2, 3): "DUAL MELODY",
    (2, 4): "PITCH",
    (4, 14): "HARMONY D",

    (5, 5): "PITCH S",
    (2, 15): "RING MOD",
    (3, 3): "TAPE MOD",
}
WAH_EFFECTS = {
    (0, 1): "VOX WAH",
    (0, 8): "CRY WAH",
    (0, 10): "RACK WAH",
    (0, 7): "BASS WAH",
    (0, 15): "TOUCH WAH",
    (1, 5): "AUTO WAH",
}
DRV_EFFECTS = {
    (0, 0): "SKREAMER",
    (0, 1): "SKREAMER 9",
    (0, 2): "BUTTER OD",
    (0, 4): "WARM OD",
    (0, 6): "SUPER OD",
    (0, 9): "BLUES OD",
    (0, 10): "FULL OD",
    (0, 14): "BREAKER OD",
    (1, 0): "GERDEN OD",
    (1, 14): "TIMMY OD",
    (0, 15): "MASTER OD",
    (2, 6): "SOLAR FUZZ",
    (2, 2): "FUZZ CREAM",
    (2, 4): "RED FUZZ",
    (2, 10): "JP DIST",
    (2, 11): "DARK MOUSE",
    (2, 13): "PLEXI DIST",
    (2, 14): "MASTER DIST",
    (2, 9): "DIST PLUS",
    (3, 0): "SHARK",
    (3, 2): "STRIVE",
    (5, 2): "SARDAR DIST",
    (3, 15): "BASS OD",
    (4, 0): "BASS DIST",
}
AMP_EFFECTS = {
    (0, 1): "TWD DELUXE",
    (0, 3): "B-MAN N",
    (2, 4): "B-MAN BRI",
    (0, 4): "DARK DOUBLE",
    (0, 5): "DARK DELUXE",
    (0, 15): "SUPERO 2 CL",
    (2, 8): "SUPERO 2 OD",
    (1, 0): "VOKS 15TB",
    (1, 1): "VOKS 30N",
    (2, 7): "VOKS 30TB",
    (1, 4): "JAZZ 120",
    (1, 5): "SUPERB CL",
    (4, 8): "SUPERB OD",
    (1, 9): "CALIF STAR CL",
    (4, 10): "CALIF STAR OD",
    (1, 10): "BOG SV CL",
    (3, 13): "BOG SV OD",
    (4, 3): "BOG XT BLUE",
    (6, 14): "BOG XT RED",
    (1, 11): "DOCTOR CL",
    (4, 9): "DOCTOR OD",
    (1, 15): "DRAGON CL",
    (7, 11, 7): "DRAGON CL B",
    (7, 12): "DRAGON OD",
    (2, 3): "SOL 100 CL",
    (4, 7): "SOL 100 OD",
    (5, 9): "SOL 100 LD",
    (2, 10): "BRIT 45",
    (2, 11): "BRIT 45+",
    (2, 12): "BRIT 45 JP",
    (2, 13): "BRIT 50",
    (2, 14): "BRIT 50+",
    (2, 15): "BRIT 50JP",
    (3, 0): "BRIT SLP",
    (3, 5): "BRIT 800",
    (4, 14): "BRIT 900",
    (4, 0): "FLYMAN 1",
    (4, 1): "FLYMAN 2",
    (5, 13): "FLYMAN+ 1",
    (5, 14): "FLYMAN+ 2",
    (3, 9): "CALIF IIC+ 1",
    (3, 10): "CALIF IIC+ 2",
    (3, 11): "CALIF IIC+ 3",
    (5, 5): "CALIF IV LD 1",
    (5, 6): "CALIF IV LD 2",
    (5, 7): "CALIF IV LD 3",
    (6, 8): "CALIF DUAL V",
    (6, 9): "CALIF DUAL M",
    (5, 3): "TANGER R100",
    (5, 10): "HALEN 51",
    (5, 15): "ENG 120",
    (6, 0): "ENG 120+",
    (6, 5): "DIZZY VH",
    (6, 6): "DIZZY VH S",
    (6, 10): "DIZZY VH+",
    (6, 11): "DIZZY VH+ S",
    (7, 3): "A BASSVT",
    (7, 5, 7): "VOKS BASS",
    (7, 7): "CALIF BASS",
    (7, 5, 8): "A BASSFT",
    (7, 6): "F-2BASS",
    (7, 10): "AC PREAMP",
    (7, 11, 8): "AC PREAMP2",
}
CAB_EFFECTS = {
    (0, 0): "SUPERO 1x6",
    (0, 1): "CHAP 1x8",
    (0, 2): "PRINCE 1x10",
    (1, 4): "TWD 2X10",
    (0, 11): "TWD LUX 1X12",
    (0, 3): "DARK LUX 1X12",
    (1, 2): "TWIN VERB 2X12",
    (1, 11): "CUSTOM 2X12",
    (1, 6): "BMAN 2X10",
    (1, 14): "BMAN 4X10",
    (1, 1): "JAZZ 2X12",
    (0, 14): "BRIT 1X12",
    (1, 3): "BRIT GN 2X12",
    (1, 15): "BRIT LD 4X12",
    (2, 0): "BRIT TD 4X12",
    (2, 1): "BRIT MD 4X12",
    (2, 2): "BRIT GN 4X12",
    (3, 0): "BRIT 75 4X12",
    (2, 11): "BRIT BK 4X12",
    (0, 8): "VOKS 1X12",
    (0, 15): "VOKS 2X12",
    (0, 6): "BOG SV 1X12",
    (1, 0): "CHIEF 2X12",
    (2, 4): "CALIF DUAL 4X12",
    (0, 9): "CALIF STAR 1X12",
    (1, 9): "CALIF STAR 2X12",
    (0, 12): "CALIF 1X12",
    (1, 7): "SUPERO 2X12",
    (1, 8): "SUPERB 2X12",
    (1, 13): "BLUE 2X12",
    (2, 3): "HALEN 4X12",
    (2, 5): "BOG 4X12",
    (2, 6): "ENG 4X12",
    (2, 7): "BOG UB 4X12",
    (2, 8): "SOL 4X12",
    (2, 9): "TANGER 4X12",
    (2, 10): "WATT 4X12",
    (2, 12): "WAM 4X12",
    (2, 13): "HUMBLE 4X12",
    (2, 14): "DIZZY 4X12",
    (3, 1): "CALIF 4X12",
    (3, 2): "DV 1X15",
    (3, 7): "DV 4X10",
    (3, 3): "WORK 1X15",
    (3, 9): "WORK 4X10",
    (3, 5): "CALIF 2X10",
    (3, 6): "MAK 2X10",
    (3, 4): "A BASS 1X15",
    (3, 8): "A BASS 4X10",
    (3, 11): "A BASS 8X10",
    (3, 10): "HART 4X12",
    (3, 12): "D 1",
    (3, 13): "D 2",
    (3, 14): "OM",
    (3, 15): "JUMBO",
    (4, 0): "BIRD",
    (4, 1): "GA",
    (4, 2): "CLASSICAL AC",
    (4, 3): "MANDOLIN",
    (4, 4): "FRETLESS BASS",
    (4, 5): "DOUBLE BASS",
}

def decode_preset(data):
    if len(data) < 40:
        return None

    bank_group = data[38]
    preset_slot = data[39]

    if preset_slot < 0 or preset_slot > 15:
        return None

    bank = (bank_group * 4) + (preset_slot // 4) + 1

    if bank < 1 or bank > 60:
        return None

    letter = LETTERS[preset_slot % 4]

    return {
        "type": "preset",
        "bank": bank,
        "letter": letter,
        "preset_name": f"{bank:02d}{letter}",
    }


def decode_effect_model(data):
    # DYN padrão
    if len(data) == 108 and data[8] == 48:
        effect_key = (data[58], data[59])
        effect_name = DYN_EFFECTS.get(effect_key)

        return {
            "type": "effect_model",
            "category": "DYN",
            "effect_key": effect_key,
            "effect_name": effect_name,
        }

    # FREQ / WAH
    if len(data) == 128 and data[8] == 58:
        effect_key = (data[60], data[61])
        category_id = data[49]

        if category_id == 1:
            category = "FREQ"
            effect_name = FREQ_EFFECTS.get(effect_key)

        elif category_id == 2:
            category = "WAH"
            effect_name = WAH_EFFECTS.get(effect_key)

        elif category_id == 3:
            category = "DRV"
            effect_name = DRV_EFFECTS.get(effect_key)

        elif category_id == 4:
            category = "AMP"
            effect_key = (data[60], data[61], data[67])
            effect_name = AMP_EFFECTS.get(effect_key)

        elif category_id == 5:
           category = "CAB"
           effect_name = CAB_EFFECTS.get(effect_key)

        else:
            category = f"UNKNOWN_CATEGORY_{category_id}"
            effect_name = None

        return {
            "type": "effect_model",
            "category": category,
            "category_id": category_id,
            "effect_key": effect_key,
            "effect_name": effect_name,
        }

    return None


def decode_sysex(data):
    if len(data) < 9:
        return {"type": "unknown", "reason": "too_short"}

    event_type = data[6]

    # =====================
    # STATUS / PRESET / DRUM / MODE
    # =====================

    if data[8] == 20 and len(data) >= 40:
        if data[32] == 5 and data[33] == 2:
            mode = "stomp" if data[39] == 1 else "preset"
            return {
                "type": "mode",
                "mode": mode,
            }

        if data[32] == 8 and data[33] == 1:
            playing = bool(data[39])
            return {
                "type": "drum",
                "playing": playing,
            }

        preset = decode_preset(data)
        if preset:
            return preset

    # =====================
    # EFFECT BLOCK ON/OFF
    # =====================

    if len(data) >= 48 and data[8] == 24:
        slot = data[39] + 1
        enabled = bool(data[47])

        return {
            "type": "effect_block",
            "slot": slot,
            "enabled": enabled,
        }

    # =====================
    # EFFECT MODEL
    # =====================

    effect_model = decode_effect_model(data)
    if effect_model:
        return effect_model

    # =====================
    # UNKNOWN
    # =====================

    return {
        "type": "unknown",
        "event": event_type,
        "length": len(data),
        "data8": data[8],
    }