from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

mx.set_bpm(90)
time.sleep(2)

mx.set_bpm(120)
time.sleep(2)

mx.set_bpm(180)

mx.close()