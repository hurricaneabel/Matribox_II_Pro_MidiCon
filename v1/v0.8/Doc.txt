# Matribox Controller Project - Documentação Técnica v1.0

## Objetivo do Projeto

Desenvolver uma biblioteca Python para controle completo da pedaleira Matribox II Pro através de MIDI.

O projeto foi desenvolvido utilizando testes reais em hardware, validando os comandos diretamente na pedaleira e não apenas com base no manual do fabricante.

---

# Ambiente de Desenvolvimento

## Python

Versão utilizada:

```text
Python 3.12.0
```

## Bibliotecas

```bash
pip install mido python-rtmidi
```

## Porta MIDI Detectada

```text
Matribox II Pro Subdevice 1
```

Verificação:

```python
import mido

print(mido.get_output_names())
```

---

# Arquitetura do Projeto

## matribox_core.py

Camada responsável pela comunicação MIDI direta.

Responsabilidades:

* Envio de CC (Control Change)
* Envio de Program Change
* Seleção de presets
* Controle de bancos
* Controle de módulos
* Controle do looper
* Controle da bateria
* Controle de BPM
* Controle do afinador
* Controle de expression
* Controle dos quick knobs

---

## matribox_state.py

Responsável por armazenar estado interno do software.

Armazena:

* Banco atual
* Preset atual
* Modo atual
* Estado dos módulos
* Estado do afinador

Importante:

O state NÃO lê o estado real da pedaleira.

Ele apenas registra o estado conhecido pelo software.

---

## matribox_controller.py

Camada intermediária.

Fluxo:

```text
GUI
 ↓
Controller
 ↓
Core
 ↓
MIDI
 ↓
Matribox
```

Responsabilidades:

* Coordenar operações
* Atualizar state
* Chamar funções do core

---

# Estrutura da Matribox

## Bancos

```text
01
02
03
...
60
```

Total:

```text
60 bancos
```

---

## Presets

Cada banco possui:

```text
A
B
C
D
```

Exemplo:

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

# Seleção de Presets

## MIDI

Utiliza:

```text
CC0
Program Change
```

---

## Bancos 01-30

```text
CC0 = 0
PC = 1-120
```

---

## Bancos 31-60

```text
CC0 = 1
PC = 1-120
```

---

## Fórmula Validada

```python
pc = ((bank_inside_group - 1) * 4) + letter_index + 1
```

---

# Modos

## CC29

Validado em hardware:

```text
0   = STOMP
64  = PRESET
```

Funções:

```python
set_stomp_mode()
set_preset_mode()
```

---

# Navegação MIDI Nativa

## Bancos

```text
CC22 = Bank +
CC23 = Bank -
```

## Presets

```text
CC24 = Preset +
CC25 = Preset -
```

## Wait Mode

```text
CC26 = Bank + Wait
CC27 = Bank - Wait
CC28 = Bank Wait
```

Todos validados.

---

# CTRLs

## CC71-74

```text
CC71 = CTRL1
CC72 = CTRL2
CC73 = CTRL3
CC74 = CTRL4
```

Importante:

Os CTRLs não possuem função fixa.

Eles executam as funções configuradas pelo usuário dentro de cada preset.

Exemplo:

```text
CTRL1 = Overdrive
CTRL2 = Delay
CTRL3 = Reverb
CTRL4 = Solo
```

Outro preset pode utilizar funções completamente diferentes.

---

# Módulos / Blocos

## CC43-54

```text
CC43 = Bloco 1
CC44 = Bloco 2
CC45 = Bloco 3
CC46 = Bloco 4
CC47 = Bloco 5
CC48 = Bloco 6
CC49 = Bloco 7
CC50 = Bloco 8
CC51 = Bloco 9
CC52 = Bloco 10
CC53 = Bloco 11
CC54 = Bloco 12
```

Valores:

```text
0   = OFF
127 = ON
```

Importante:

O controle é pela posição do bloco na cadeia.

Não importa se o bloco é:

```text
Amp
Cab
Delay
Reverb
EQ
Compressor
```

Sempre será controlado pela posição.

---

# Afinador

## CC58

```text
0   = OFF
127 = ON
```

Validado.

---

# Preset Volume

## CC7

```text
0-100
```

Mudança instantânea.

Validado.

---

# Expression

## Posição do Pedal

CC11

```text
0-100
```

Representa a posição virtual do pedal.

Exemplo:

```text
0   = Heel
50  = Meio
100 = Toe
```

---

## Troca A/B

CC13

```text
0-63   = A
64-127 = B
```

Equivale ao botão físico do pedal.

Exemplo:

```text
EXP A = Volume
EXP B = Wah
```

Validado.

---

# Quick Access Knobs

## Valores Diretos

```text
CC16 = Knob 1
CC18 = Knob 2
CC20 = Knob 3
```

Faixa:

```text
0-100
```

---

## Incremento / Decremento

```text
CC17 = Knob 1 Step
CC19 = Knob 2 Step
CC21 = Knob 3 Step
```

Valores:

```text
0-63   = -1 passo
64-127 = +1 passo
```

Validado.

---

# BPM

## BPM Direto

CC68 + CC69

Faixa:

```text
40-300 BPM
```

Mudança instantânea.

Validado.

---

## Tap Tempo

CC70

```text
127
```

Valida o BPM pelo intervalo entre taps.

Fórmula:

```python
interval = 60 / bpm
```

Exemplos:

```text
60 BPM  = 1.0s
120 BPM = 0.5s
180 BPM = 0.333s
```

---

# Looper

## ON/OFF

CC59

```text
0   = OFF
127 = ON
```

---

## Record

CC60

---

## Auto Record

CC61

Validado.

---

## Play / Stop

CC62

```text
127 = Play
0   = Stop
```

---

## Undo / Redo

CC63

Validado.

---

## Delete Loop

CC64

Validado.

---

## Recording Volume

CC65

```text
0-100
```

---

## Playback Volume

CC66

```text
0-100
```

---

## Placement

CC67

```text
0   = POST
127 = PRE
```

Validado.

---

# Drum Machine

## Menu

CC92

```text
127 = Abrir
0   = Fechar
```

---

## Play / Stop

CC93

```text
127 = Play
0   = Stop
```

Funciona mesmo sem abrir o menu.

---

## Rhythm

CC94

```text
0-99
```

Troca imediata.

Validado.

---

## Volume

CC95

```text
0-100
```

Funciona sem abrir o menu.

Validado.

---

# Descobertas Importantes

## 1

A implementação real da Matribox corresponde ao manual em praticamente todos os comandos testados.

---

## 2

Os blocos 1-12 representam posições da cadeia e não tipos de efeitos.

---

## 3

CTRLs e Quick Knobs são totalmente configuráveis pelo usuário.

O software apenas aciona as funções configuradas.

---

## 4

A bateria pode tocar sem abrir sua interface.

---

## 5

O BPM pode ser alterado diretamente sem troca de preset.

---

## 6

O software atualmente envia comandos MIDI.

A leitura do estado real da pedaleira ainda não foi implementada.

---

# Status do Projeto

## MatriboxCore

```text
STATUS: CONCLUÍDO
VERSÃO: 1.0
```

Todos os comandos relevantes do manual foram testados e validados em hardware real.

---

# Próximas Fases

## Fase 2

Funcionalidades avançadas:

```text
Macros
Automações
Scenes
Looper automático
Drum + Looper sincronizados
```

---

## Fase 3

Interface:

```text
GUI Desktop
Controle Web
Controle por Celular
Show Mode
Setlists
```

---

# Resultado

Foi criada uma biblioteca Python capaz de controlar praticamente todos os recursos MIDI relevantes da Matribox II Pro através de testes reais e validação em hardware.
