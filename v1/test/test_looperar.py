from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("Abrindo Looper")
mx.core.looper_on()
time.sleep(2)

print("Auto Record")
mx.core.looper_auto_record()
time.sleep(8)

print("Play")
mx.core.looper_play()
time.sleep(5)

print("Stop")
mx.core.looper_stop()
time.sleep(1)

print("Delete")
mx.core.looper_delete()
time.sleep(1)

print("Fechando Looper")
mx.core.looper_off()

mx.close()