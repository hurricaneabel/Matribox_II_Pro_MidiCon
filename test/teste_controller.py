from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

mx.go_to_preset(1, "A")
time.sleep(1)

mx.select_b()
time.sleep(1)

mx.next_bank()
time.sleep(1)

mx.toggle_module(1)
time.sleep(1)

mx.toggle_module(1)
time.sleep(1)

mx.toggle_tuner()
time.sleep(1)

mx.toggle_tuner()

mx.close()