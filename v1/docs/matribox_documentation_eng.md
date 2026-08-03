# Matribox Controller Project - Technical Documentation v1.0

## Project Objective

To develop a Python library for complete control of the Matribox II Pro pedalboard via MIDI.

The project was developed using real-world hardware testing, validating the commands directly on the pedalboard and not just based on the manufacturer's manual.

---

# Development Environment

## Python

Version used:

```text
Python 3.12.0
```

## Libraries

```bash.pip install mido python-rtmidi
```

## MIDI Port Detected

```text
Subdevice 1 of Matribox II Pro

```

Verification:

```python.import mido

print(mido.get_output_names())

```

---

# Project Architecture

## matribox_core.py

Layer responsible for direct MIDI communication.

Responsibilities:

* Control Change Sending
* Program Change Sending
* Preset Selection
* Bank Control
* Module Control
* Looper Control
* Drum Control
* BPM Control
* Tuner Control
* Expression Control
* Quick Button Control

---

## matribox_state.py

Responsible for storing the software's internal state.

Store:

* Current Bank
* Current Preset
* Current Mode
* Module State
* Funder State

Important:

The state does NOT read the actual state of the pedalboard.

It only registers the state known to the software.

---

## matribox_controller.py

Intermediate Layer.

Flow:

```text
GUI ↓
Controller ↓
Essential ↓
MIDI ↓
Matrix Box
```

Responsibilities:

* Operations Coordinator
* Update State
* Call Core Functions

---

#Matrix Structure

##Banks

```text
01
02
03
...
60
```

Total:

```text
60 banks
```

---

##Presets

Each bank Contains:

```text
A
B
C
D
```

Example:

```text
01A
01B
01C
01D

02A
02B
02C
02D
```

Total:

```text
240 presets
```

---

# Preset Selection

##MIDI

Use:

```text
CC0
Program Change
```

---

## Banks 01-30

```text
CC0 = 0
PC = 1-120
```

---

## Banks 31-60

```text
CC0 = 1
PC = 1-120
```

---

##Formula Validated

```python
pc = ((bank_inside_group - 1) * 4) + letter_index + 1

```

---

#Modes

## CC29

Hardware validated:

```text
0 = PASS
64 = PRESET
```

Functions:

```python
set_stomp_mode()
set_preset_mode()
```

---

# Native MIDI Navigation

##Banks

```text
CC22 = Bank +
CC23 = Bank -

```

## Presets

```text
CC24 = Preset +
CC25 = Preset -

```

## Standby Mode

```text
CC26 = Bank + Standby
CC27 = Bank - Please wait
CC28 = Bank Wait
```

All validated.

---

#CTRLs

## CC71-74

```text
CC71 = CTRL1
CC72 = CTRL2
CC73 = CTRL3
CC74 = CTRL4
```

Important:

CTRLs do not have a fixed function.

They execute the functions defined by the user within each preset.

Example:

```text
CTRL1 = Overshoot
CTRL2 = Delay
CTRL3 = Reverb
CTRL4 = Solo
```

Another preset may use completely different functions.

---

# Modules / Blocks

## CC43-54

```text
CC43 = Block 1
CC44 = Block 2
CC45 = Block 3
CC46 = Block 4
CC47 = Block 5
CC48 = Block 6
CC49 = Block 7
CC50 = Block 8
CC51 = Block 9
CC52 = Block 10
CC53 = Block 11
CC54 = Block 12
```

Values:

```text
0 = OFF
127 = ON
```

Important:

Control is by the block's position in the chain.

It doesn't matter if the block is:

```text
Amplifier
Taxi
Delay
Reverb
Equalization
Compressor
```

It will always be controlled by its position.

---

# Tuner

## CC58

```text
0 = OFF
127 = ON
```

Validated.

--

# Preset Volume

##CC7

```text
0-100
```

Instant change.

Validated.

--

# Expression

## Pedal Position

CC11

```text
0-100
```

Represents the virtual pedal position.

Example:

```text
0 = Heel
50 = Middle
100 = Toe
```

---

## A/B Switch

CC13

```text
0-63 = A
64-127 = B
```

Equivalent to the physical pedal button.

Example:

```text
EXP A = Volume
EXP B = Wow
```

Validated.

---

# Quick Access Buttons

## Direct Values

```text
CC16 = Button 1
CC18 = Button 2
CC20 = Button 3
```

Range:

```text
0-100
```

---

## Increment / Decrement

```text
CC17 = Button 1 Step
CC19 = Button 2 Step
CC21 = Button 3 Step
```

Values:

```text
0-63 = -1 steps
64-127 = +1 step
```

Validated.

---

#BPM

##Direct BPM

CC68 + CC69

Range:

```text
40-300 BPM

```

Instant change.

Validated.

--

## Tempo Tap

CC70

```text
127

```

Validates the BPM by the interval between taps.

Formula:

```python
interval = 60/bpm

```

Examples:

```text
60 BPM = 1.0s
120 BPM = 0.5s
180 BPM = 0.333s

```

---

# Looper

## ON/OFF

CC59

```text
0 = OFF
127 = ON

```

---

## Record

CC60

---

## Automatic Recording

CC61

Validated.

---

## Play / Stop

CC62

```text
127 = Play
0 = Stop

```

---

## Undo/Redo

CC63

Validated.

---

## Delete loop

CC64

Validated.

--

## Recording volume

CC65

```text
0-100
```

---

## Playback volume

CC66

```text
0-100
```

---

## Placement

CC67

```text
0 = POST
127 = P