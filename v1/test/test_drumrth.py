from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Abrindo Drum")
mx.core.send_cc(92, 127)
time.sleep(2)

print("Play")
mx.core.send_cc(93, 127)
time.sleep(3)

for rhythm in [0, 10, 20, 30, 40]:
    print(f"Rhythm {rhythm}")
    mx.core.send_cc(94, rhythm)
    time.sleep(5)

print("Stop")
mx.core.send_cc(93, 0)
time.sleep(2)

print("Fechando Drum")
mx.core.send_cc(92, 0)

mx.close()