from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Abrindo Looper")
mx.core.send_cc(59, 127)
time.sleep(2)

print("Record")
mx.core.send_cc(60, 127)
time.sleep(5)

print("Play")
mx.core.send_cc(62, 127)
time.sleep(5)

print("Stop")
mx.core.send_cc(62, 0)
time.sleep(2)

print("Delete Loop")
mx.core.send_cc(64, 127)
time.sleep(2)

print("Fechando Looper")
mx.core.send_cc(59, 0)

mx.close()