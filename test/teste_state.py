from matribox_state import MatriboxState

state = MatriboxState()

print(state.preset_name)

state.set_preset(12, "C")
print(state.preset_name)

print(state.modules)

novo_estado = state.toggle_module(3)
print("Módulo 3:", novo_estado)

novo_estado = state.toggle_tuner()
print("Afinador:", novo_estado)