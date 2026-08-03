from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("EXP1 MSB = 0")
mx.core.send_cc(11, 0)
time.sleep(3)

print("EXP1 MSB = 50")
mx.core.send_cc(11, 50)
time.sleep(3)

print("EXP1 MSB = 100")
mx.core.send_cc(11, 100)
time.sleep(3)

print("EXP1 A/B = 0 (A)")
mx.core.send_cc(13, 0)
time.sleep(3)

print("EXP1 A/B = 63 (A)")
mx.core.send_cc(13, 63)
time.sleep(3)

print("EXP1 A/B = 64 (B)")
mx.core.send_cc(13, 64)
time.sleep(3)

print("EXP1 A/B = 127 (B)")
mx.core.send_cc(13, 127)

mx.close()