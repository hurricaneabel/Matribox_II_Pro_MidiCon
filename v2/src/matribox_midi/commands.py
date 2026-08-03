"""
Constantes dos comandos MIDI documentados para a Matribox II Pro.

Este módulo mantém os números MIDI centralizados, evitando que valores
numéricos fiquem espalhados pelo projeto.

Referência:
    Manual da Matribox II Pro — MIDI Control Information List.
"""

from __future__ import annotations

from enum import IntEnum


class ControlChange(IntEnum):
    """
    Controles MIDI gerais reconhecidos pela Matribox II Pro.
    """
    BANK_SELECT = 0
    PRESET_VOLUME = 7
    EXPRESSION = 11
    EXPRESSION_1_A_B = 13
    BANK_UP = 22
    BANK_DOWN = 23
    PRESET_NEXT = 24
    PRESET_PREVIOUS = 25
    PRESET_STOMP_MODE = 29
    TAP_TEMPO = 70
    PRESET_BPM_MSB = 68
    PRESET_BPM_LSB = 69
    LOOPER = 59
    LOOPER_RECORD = 60
    LOOPER_PLAY_STOP = 62
    LOOPER_DELETE = 64
    LOOPER_UNDO_REDO = 63
    LOOPER_AUTO_RECORD = 61
    TUNER = 58

class StompControl(IntEnum):
    """
    Controles MIDI dos quatro footswitches configuráveis.

    No modo Stomp, cada controle executa a ação definida no preset atual.
    Uma ação pode controlar um ou vários módulos de efeito.
    """

    CONTROL_1 = 71
    CONTROL_2 = 72
    CONTROL_3 = 73
    CONTROL_4 = 74

class EffectModule(IntEnum):
    """
    Controles MIDI dos 12 módulos de efeito da Matribox II Pro.

    Cada valor representa o número de Control Change correspondente ao
    módulo indicado.
    """

    MODULE_1 = 43
    MODULE_2 = 44
    MODULE_3 = 45
    MODULE_4 = 46
    MODULE_5 = 47
    MODULE_6 = 48
    MODULE_7 = 49
    MODULE_8 = 50
    MODULE_9 = 51
    MODULE_10 = 52
    MODULE_11 = 53
    MODULE_12 = 54


class OperatingModeValue(IntEnum):
    """
    Valores MIDI usados para selecionar o modo de operação da pedaleira.

    Segundo o manual:

    - valores de 0 a 63 selecionam o modo Preset;
    - valores de 64 a 127 selecionam o modo Stomp.

    O projeto utiliza 0 e 127 para representar cada modo.
    """

    PRESET = 0
    STOMP = 127

class SwitchValue(IntEnum):
    """
    Valores utilizados para ligar e desligar funções da pedaleira.

    Segundo o manual:

    - valores de 0 a 63 representam desligado;
    - valores de 64 a 127 representam ligado.

    O projeto utiliza 0 e 127 para tornar a intenção mais clara.
    """

    OFF = 0
    ON = 127