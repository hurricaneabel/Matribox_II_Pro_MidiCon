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