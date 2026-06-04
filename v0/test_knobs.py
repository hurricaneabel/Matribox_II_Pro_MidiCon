from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Quick Knob 1 = 20")
mx.core.send_cc(16, 20)
time.sleep(3)

print("Quick Knob 1 = 80")
mx.core.send_cc(16, 80)
time.sleep(3)

print("Quick Knob 2 = 20")
mx.core.send_cc(18, 20)
time.sleep(3)

print("Quick Knob 2 = 80")
mx.core.send_cc(18, 80)
time.sleep(3)

print("Quick Knob 3 = 20")
mx.core.send_cc(20, 20)
time.sleep(3)

print("Quick Knob 3 = 80")
mx.core.send_cc(20, 80)


mx.close()