from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Enviando 4 taps em 120 BPM aproximado...")

for i in range(4):
    print(f"Tap {i + 1}")
    mx.core.send_cc(70, 127)
    time.sleep(0.332)  # 0.5s entre taps = 120 BPM

mx.close()