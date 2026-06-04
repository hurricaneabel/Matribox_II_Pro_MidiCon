import mido

print("Entradas disponíveis:")
for name in mido.get_input_names():
    print(name)

port_name = "Matribox II Pro Subdevice 0"

with mido.open_input(port_name) as port:
    print("Escutando MIDI...")
    for msg in port:
        print(msg)