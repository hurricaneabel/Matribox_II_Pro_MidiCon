from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Abrindo Looper")
mx.core.send_cc(59, 127)
time.sleep(2)

print("Volume de gravação 30")
mx.core.send_cc(65, 30)
time.sleep(2)

print("Volume de gravação 100")
mx.core.send_cc(65, 100)
time.sleep(2)

print("Volume de playback 30")
mx.core.send_cc(66, 30)
time.sleep(2)

print("Volume de playback 100")
mx.core.send_cc(66, 100)
time.sleep(2)

print("Fechando Looper")
mx.core.send_cc(59, 0)

mx.close()