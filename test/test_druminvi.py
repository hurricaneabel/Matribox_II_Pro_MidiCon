from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Play bateria sem abrir menu")
mx.core.send_cc(93, 127)

time.sleep(5)

print("Stop bateria")
mx.core.send_cc(93, 0)

mx.close()