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
    TUNER = 58


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