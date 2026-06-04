from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

mx.go_to_preset(1, "A")
time.sleep(1)

mx.set_bpm(120)
time.sleep(1)

mx.preset_volume(80)
time.sleep(1)

mx.quick_knob(1, 50)
time.sleep(1)

mx.quick_knob_up(1)
time.sleep(1)

mx.module_on(1)
time.sleep(1)

mx.module_off(1)
time.sleep(1)

mx.tuner_on()
time.sleep(1)

mx.tuner_off()

mx.close()