from matribox_core import MatriboxCore
import time

mx = MatriboxCore("Matribox II Pro Subdevice 1")

mx.module_off(8)
time.sleep(3)

mx.module_on(8)

mx.close()