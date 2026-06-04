from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Volume preset 30")
mx.core.send_cc(7, 30)
time.sleep(4)

print("Volume preset 80")
mx.core.send_cc(7, 80)
time.sleep(4)

print("Volume preset 100")
mx.core.send_cc(7, 100)

mx.close()