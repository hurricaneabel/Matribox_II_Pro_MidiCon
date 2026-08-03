from matribox_core import MatriboxCore
import time

mx = MatriboxCore("Matribox II Pro Subdevice 1")

valores = [0]

for valor in valores:
    print(f"Enviando CC29 valor {valor}")
    mx.send_cc(29, valor)
    time.sleep(4)

mx.close()