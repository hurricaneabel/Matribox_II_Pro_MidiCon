import mido

port_name = "Matribox II Pro Subdevice 0"

with mido.open_input(port_name) as port:
    print("Escutando MIDI...")
    print("Troque manualmente: 12A, 12B, 12C, 12D, depois 13A.")
    for msg in port:
        if msg.type == "sysex":
            data = list(msg.data)
            print(data)
        else:
            print(msg)