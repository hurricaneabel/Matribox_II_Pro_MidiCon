import mido

port_name = "Matribox II Pro Subdevice 0"


def decode_sysex(data):
    event_type = data[6]

    if event_type == 30:
        return "Modo PRESET"

    if event_type == 31:
        return "Modo STOMP"

    return f"Evento SysEx desconhecido ({event_type})"


with mido.open_input(port_name) as port:
    print("Escutando tudo...")

    for msg in port:
        print()
        print("MSG:", msg)

        if msg.type == "sysex":
            data = list(msg.data)
            print("RAW:", data)
            print("DECODE:", decode_sysex(data))