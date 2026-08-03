from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Abrindo Looper")
mx.core.send_cc(59, 127)
time.sleep(2)

print("Gravando loop base por 5s")
mx.core.send_cc(60, 127)
time.sleep(5)

print("Tocando loop")
mx.core.send_cc(62, 127)
time.sleep(3)

print("Gravando overdub por 5s")
mx.core.send_cc(60, 127)
time.sleep(5)

print("Finalizando overdub / voltando para play")
mx.core.send_cc(62, 127)
time.sleep(3)

print("UNDO/REDO")
mx.core.send_cc(63, 127)
time.sleep(5)

print("UNDO/REDO de novo")
mx.core.send_cc(63, 127)
time.sleep(5)

print("Stop")
mx.core.send_cc(62, 0)
time.sleep(1)

print("Delete Loop")
mx.core.send_cc(64, 127)
time.sleep(1)

print("Fechando Looper")
mx.core.send_cc(59, 0)

mx.close()