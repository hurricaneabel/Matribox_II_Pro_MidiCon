from matribox_controller import MatriboxController
import time

mx = MatriboxController("Matribox II Pro Subdevice 1")

print("=== PRESET ===")
mx.go_to_preset(12, "C")
time.sleep(5)

print("=== MODO PRESET ===")
mx.set_preset_mode()
time.sleep(5)

print("=== BPM 120 ===")
mx.set_bpm(120)
time.sleep(5)

print("=== PRESET VOLUME 80 ===")
mx.preset_volume(80)
time.sleep(5)

print("=== EXP 50 ===")
mx.exp1(50)
time.sleep(5)

print("=== EXP B ===")
mx.exp1_b()
time.sleep(5)

print("=== QUICK KNOB 1 = 75 ===")
mx.quick_knob(1, 75)
time.sleep(5)

print("=== MODULO 3 ON ===")
mx.module_on(3)
time.sleep(5)

print("=== DRUM PLAY ===")
mx.drum_play()
time.sleep(5)

print("=== DRUM RHYTHM 10 ===")
mx.drum_rhythm(10)
time.sleep(5)

print("=== DRUM VOLUME 70 ===")
mx.drum_volume(70)
time.sleep(5)

print()
print("===== STATE =====")
print("Preset:", mx.state.preset_name)
print("Modo:", mx.state.mode)

print("BPM:", mx.state.bpm)
print("Volume:", mx.state.preset_volume)

print("EXP:", mx.state.exp1_value)
print("EXP Mode:", mx.state.exp1_mode)

print("Knob1:", mx.state.quick_knobs[1])

print("Modulo 3:", mx.state.modules[3])

print("Drum Playing:", mx.state.drum_playing)
print("Drum Rhythm:", mx.state.drum_rhythm)
print("Drum Volume:", mx.state.drum_volume)

mx.close()