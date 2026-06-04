import mido

LETTERS = ["A", "B", "C", "D"]

port_name = "Matribox II Pro Subdevice 0"


def decode_preset(data):
    if len(data) < 40:
        return None

    bank_group = data[38]
    preset_slot = data[39]

    bank = (bank_group * 4) + (preset_slot // 4) + 1
    letter = LETTERS[preset_slot % 4]

    return bank, letter


with mido.open_input(port_name) as port:
    print("Escutando SysEx...")
    print("Troque presets na pedaleira.")

    for msg in port:
        if msg.type == "sysex":
            data = list(msg.data)
            decoded = decode_preset(data)

            print()
            print("SysEx:", data)

            if decoded:
                bank, letter = decoded
                print(f"Preset detectado: {bank:02d}{letter}")
        else:
            print(msg)