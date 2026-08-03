# Matribox II Pro MIDI Controller — V2

Esta pasta contém a reconstrução do controlador MIDI para a pedaleira Matribox II Pro.

## Objetivo

Criar uma biblioteca simples, estável e bem documentada para enviar comandos MIDI à Matribox II Pro.

A V2 será inicialmente responsável apenas pelo envio de comandos. Ela não tentará receber informações da pedaleira nem sincronizar estados em tempo real.

## Estado atual

Projeto em reconstrução.

## Estrutura

- `src/`: código principal da biblioteca.
- `tools/`: ferramentas de diagnóstico e desenvolvimento.
- `tests/`: testes automatizados.
- `docs/`: documentação técnica do projeto.
- `requirements.txt`: dependências Python.

## Versão anterior

O código antigo está preservado na pasta `v1/` para consulta e referência.

## Recursos implementados

A versão 2 já permite controlar a Matribox II Pro por MIDI USB.

### Presets

- Seleção direta dos 240 presets
- Bancos de 01 a 60
- Presets A, B, C e D
- Próximo preset e preset anterior
- Banco acima e banco abaixo

### Modos e controles

- Modo Preset
- Modo Stomp
- Controles Stomp 1 a 4
- Ativação dos 12 módulos de efeito
- Afinador

### Quick Access

Os três knobs Quick Access podem ser controlados de duas formas:

- Definição direta de valor entre 0 e 100
- Aumento ou redução de um passo

### Volume e expressão

- Volume do preset entre 0 e 100
- Expressão entre 0 e 100
- Seleção EXP1 A/B

### Tempo

- Definição direta de BPM entre 40 e 300
- Tap Tempo

### Looper

- Abrir e fechar o menu
- Gravação manual
- Gravação automática
- Reprodução e parada
- Undo e redo
- Exclusão da gravação
- Volume de gravação
- Volume de reprodução
- Posição PRE e POST

### Bateria

- Abrir e fechar o menu
- Iniciar e parar
- Selecionar ritmo
- Ajustar volume

## Exemplo básico

```python
from matribox_midi import MatriboxController


with MatriboxController() as controller:
    controller.select_preset(1, "A")
    controller.set_preset_volume(80)
    controller.set_bpm(120)
```

## Testes

Os testes automáticos não precisam da Matribox conectada.

```powershell
python -m unittest discover -s v2/tests -v
```