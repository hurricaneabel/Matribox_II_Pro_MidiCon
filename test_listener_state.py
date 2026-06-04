import time

from matribox_state import MatriboxState
from matribox_listener import MatriboxListener

state = MatriboxState()

listener = MatriboxListener(
    input_port_name="Matribox II Pro Subdevice 0",
    state=state,
)

listener.start()

print("Listener rodando.")
print("Mexa na pedaleira: presets, modo, drum, blocos.")
print("Pressione CTRL+C para sair.")

try:
    while True:
        print()
        print("===== STATE =====")
        print("Preset:", state.preset_name)
        print("Modo:", state.mode)
        print("Drum:", state.drum_playing)
        print("Módulos:", state.modules)

        time.sleep(5)

except KeyboardInterrupt:
    listener.stop()
    print("Listener parado.")