from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Abrindo Looper")
mx.core.send_cc(59, 127)
time.sleep(2)

print("POST")
mx.core.send_cc(67, 0)
time.sleep(5)

print("PRE")
mx.core.send_cc(67, 127)
time.sleep(5)

print("Fechando Looper")
mx.core.send_cc(59, 0)

mx.close()