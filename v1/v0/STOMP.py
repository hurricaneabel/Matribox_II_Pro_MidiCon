from matribox_core import MatriboxCore
import time

mx = MatriboxCore("Matribox II Pro Subdevice 1")

mx.set_stomp_mode()

mx.close()