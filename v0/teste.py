import mido
import time

PORTA = "Matribox II Pro Subdevice 1"

out = mido.open_output(PORTA)

# CC 24 = Preset +
out.send(mido.Message(
    "control_change",
    channel=0,
    control=24,
    value=127
))

print("Comando Preset + enviado.")
time.sleep(0.2)
out.close()