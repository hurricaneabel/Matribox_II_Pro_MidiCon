from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

testes = [
    (22, "BANK +"),
    (23, "BANK -"),
    (24, "PRESET +"),
    (25, "PRESET -"),
    (26, "BANK + wait mode"),
    (27, "BANK - wait mode"),
    (28, "BANK wait mode"),
]

for cc, nome in testes:
    print(f"Testando {nome} | CC{cc}")
    mx.core.send_cc(cc, 127)
    time.sleep(4)

mx.close()