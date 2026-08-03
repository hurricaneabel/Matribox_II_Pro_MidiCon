"""
Teste manual do controle dos módulos de efeito.

O teste liga o módulo de efeito 1, aguarda dois segundos e depois o desliga.
"""

from __future__ import annotations

import time

from matribox_midi.commands import EffectModule
from matribox_midi.controller import MatriboxController


def main() -> None:
    """Liga e desliga o primeiro módulo de efeito."""
    with MatriboxController() as matribox:
        print(f"Conectado em: {matribox.port_name}")

        print("Ligando o módulo de efeito 1...")
        matribox.effect_module_on(EffectModule.MODULE_1)

        time.sleep(2)

        print("Desligando o módulo de efeito 1...")
        matribox.effect_module_off(EffectModule.MODULE_1)

    print("Teste concluído e conexão encerrada.")


if __name__ == "__main__":
    main()