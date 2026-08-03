"""
Constantes dos comandos MIDI documentados para a Matribox II Pro.

A finalidade deste módulo é manter os números de Control Change em um único
local. Assim, o restante do projeto não precisa espalhar números MIDI pelo
código.

Referência:
    Manual oficial da Matribox II Pro — MIDI Control Information List.
"""

from __future__ import annotations

from enum import IntEnum


class ControlChange(IntEnum):
    """
    Números de Control Change reconhecidos pela Matribox II Pro.

    Esta lista será ampliada gradualmente conforme cada função for
    implementada e testada no equipamento real.
    """

    TUNER = 58


class SwitchValue(IntEnum):
    """
    Valores padronizados usados em controles de ligar e desligar.

    Segundo o manual:

    - valores de 0 a 63 representam desligado;
    - valores de 64 a 127 representam ligado.

    Usamos os extremos 0 e 127 para deixar a intenção explícita.
    """

    OFF = 0
    ON = 127