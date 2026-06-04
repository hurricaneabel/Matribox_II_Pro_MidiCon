import mido
from matribox_sysex import decode_sysex

port_name = "Matribox II Pro Subdevice 0"

with mido.open_input(port_name) as port:
    print("Escutando tudo...")

    for msg in port:
        print()

        if msg.type == "sysex":
            data = list(msg.data)
            print("RAW:", data)
            print("DECODE:", decode_sysex(data))
        else:
            print("MSG:", msg)