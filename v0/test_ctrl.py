from matribox_core import MatriboxCore
import time

PORTA = "Matribox II Pro Subdevice 1"

mx = MatriboxCore(PORTA)

mx.go_to_preset(1, "C")
time.sleep(1)

print("Enviando CTRL1")
mx.ctrl(1)
time.sleep(1)

print("Enviando CTRL2")
mx.ctrl(2)
time.sleep(1)

print("Enviando CTRL3")
mx.ctrl(3)
time.sleep(1)

print("Enviando CTRL4")
mx.ctrl(4)

mx.close()