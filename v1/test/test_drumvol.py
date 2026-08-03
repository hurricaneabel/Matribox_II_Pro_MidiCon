from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Play bateria")
mx.core.send_cc(93, 127)
time.sleep(2)

print("Volume 30")
mx.core.send_cc(95, 30)
time.sleep(4)

print("Volume 100")
mx.core.send_cc(95, 100)
time.sleep(4)

print("Stop bateria")
mx.core.send_cc(93, 0)

mx.close()