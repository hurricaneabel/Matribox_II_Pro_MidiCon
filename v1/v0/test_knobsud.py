from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Incremento/Decremento Quick Knob 1")
print("Desce 1 passo")
mx.core.send_cc(17, 0)   # 0-63 = desce 1 passo
time.sleep(2)

print("Sobe 1 passo")
mx.core.send_cc(17, 64)  # 64-127 = sobe 1 passo
time.sleep(2)

print("Incremento/Decremento Quick Knob 2")
print("Desce 1 passo")
mx.core.send_cc(19, 0)
time.sleep(2)

print("Sobe 1 passo")
mx.core.send_cc(19, 64)
time.sleep(2)

print("Incremento/Decremento Quick Knob 3")
print("Desce 1 passo")
mx.core.send_cc(21, 0)
time.sleep(2)

print("Sobe 1 passo")
mx.core.send_cc(21, 64)
time.sleep(2)

mx.close()