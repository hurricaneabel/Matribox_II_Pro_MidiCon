LETTERS = ["A", "B", "C", "D"]


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


def decode_sysex(data):
    if len(data) < 9:
        return {"type": "unknown", "reason": "too_short"}

    event_type = data[6]

    # =====================
    # STATUS / PRESET / DRUM / MODE
    # =====================

    if data[8] == 20 and len(data) >= 40:
        # Modo Stomp/Preset
        if data[32] == 5 and data[33] == 2:
            mode = "stomp" if data[39] == 1 else "preset"
            return {
                "type": "mode",
                "mode": mode,
            }

        # Drum Play/Stop
        if data[32] == 8 and data[33] == 1:
            playing = bool(data[39])
            return {
                "type": "drum",
                "playing": playing,
            }

        # Preset
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
    # UNKNOWN
    # =====================

    return {
        "type": "unknown",
        "event": event_type,
        "length": len(data),
        "data8": data[8],
    }