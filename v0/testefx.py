from matribox_core import MatriboxCore
import time

mx = MatriboxCore("Matribox II Pro Subdevice 1")

# Escolha um preset onde você consiga ouvir/ver bem os efeitos

for cc in range(43, 55):
    modulo = cc - 42

    print(f"\nTestando módulo {modulo} | CC{cc}")

    print("Desligando...")
    mx.send_cc(cc, 0)
    time.sleep(3)

    print("Ligando...")
    mx.send_cc(cc, 127)
    time.sleep(3)

mx.close()