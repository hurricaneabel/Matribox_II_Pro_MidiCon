from matribox_core import MatriboxCore
import time

PORTA = "Matribox II Pro Subdevice 1"

mx = MatriboxCore(PORTA)

mx.set_stomp_mode()
time.sleep(0.5)

mx.go_to_preset(1, "A")
time.sleep(1)

mx.go_to_preset(1, "B")
time.sleep(1)

mx.go_to_preset(1, "C")
time.sleep(1)

mx.go_to_preset(1, "D")
time.sleep(1)

mx.go_to_preset(2, "A")
time.sleep(1)

mx.go_to_preset(31, "A")
time.sleep(1)

mx.go_to_preset(60, "D")

mx.close()