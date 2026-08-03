"""
Funções relacionadas à localização de portas MIDI.

Este módulo não envia comandos MIDI. Sua responsabilidade é apenas consultar
as portas disponíveis no sistema e localizar uma saída pertencente à
Matribox II Pro.
"""

from __future__ import annotations

import mido


# Trecho que normalmente aparece no nome da porta MIDI da pedaleira.
DEFAULT_DEVICE_NAME = "Matribox II Pro"


def list_output_ports() -> list[str]:
    """
    Retorna todas as portas MIDI de saída disponíveis no sistema.

    Returns:
        Lista com os nomes das portas MIDI encontradas. Caso nenhuma porta
        esteja disponível, retorna uma lista vazia.
    """
    return list(mido.get_output_names())


def find_matribox_output(
    device_name: str = DEFAULT_DEVICE_NAME,
) -> str | None:
    """
    Procura uma porta MIDI de saída correspondente à Matribox II Pro.

    A busca não diferencia letras maiúsculas de minúsculas. Isso torna o
    código um pouco mais resistente a diferenças no nome apresentado pelo
    sistema operacional.

    Args:
        device_name:
            Texto que deve existir no nome da porta MIDI. Por padrão, procura
            por "Matribox II Pro".

    Returns:
        Nome completo da primeira porta encontrada ou None caso a pedaleira
        não seja localizada.
    """
    expected_name = device_name.casefold()

    for port_name in list_output_ports():
        if expected_name in port_name.casefold():
            return port_name

    return None