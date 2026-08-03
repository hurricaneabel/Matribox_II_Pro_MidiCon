"""
Teste manual dos 12 módulos de efeito da Matribox II Pro.

Cada módulo será:

1. ligado;
2. mantido ligado por dois segundos;
3. desligado;
4. seguido pelo próximo módulo.

Atenção:
    Ao terminar, todos os módulos testados ficarão desligados.
"""

from __future__ import annotations

import time

from matribox_midi.commands import EffectModule
from matribox_midi.controller import MatriboxController


ACTIVE_TIME_SECONDS = 2
INTERVAL_TIME_SECONDS = 1


def main() -> None:
    """Testa sequencialmente os 12 módulos de efeito."""
    with MatriboxController() as matribox:
        print(f"Conectado em: {matribox.port_name}")
        print("Iniciando teste dos módulos...\n")

        for position, module in enumerate(EffectModule, start=1):
            print(
                f"[{position}/12] Ligando {module.name} "
                f"(Control Change {module.value})..."
            )

            matribox.effect_module_on(module)
            time.sleep(ACTIVE_TIME_SECONDS)

            print(f"[{position}/12] Desligando {module.name}...\n")

            matribox.effect_module_off(module)
            time.sleep(INTERVAL_TIME_SECONDS)

    print("Teste dos 12 módulos concluído.")
    print("Conexão MIDI encerrada.")


if __name__ == "__main__":
    main()