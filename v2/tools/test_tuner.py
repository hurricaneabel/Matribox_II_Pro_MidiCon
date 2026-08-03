"""
Teste manual do controle de alto nível do afinador.

Este teste utiliza MatriboxController, sem trabalhar diretamente com
números de Control Change ou valores MIDI.
"""

from __future__ import annotations

import time

from matribox_midi.controller import MatriboxController


def main() -> None:
    """Liga o afinador por dois segundos e depois o desliga."""
    with MatriboxController() as matribox:
        print(f"Conectado em: {matribox.port_name}")

        print("Ligando o afinador...")
        matribox.tuner_on()

        time.sleep(2)

        print("Desligando o afinador...")
        matribox.tuner_off()

    print("Teste concluído e conexão encerrada.")


if __name__ == "__main__":
    main()