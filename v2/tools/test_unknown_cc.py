"""
Teste rápido de um Control Change ainda não documentado.

Uso:
    python v2/tools/test_unknown_cc.py 57

O programa envia:

1. valor 127 para tentar ativar;
2. aguarda três segundos;
3. valor 0 para tentar desativar.

O Looper deve ser aberto manualmente antes do teste.
"""

from __future__ import annotations

import argparse
import time

from matribox_midi.midi_output import MatriboxMidiOutput


TEST_DELAY_SECONDS = 3


def parse_arguments() -> argparse.Namespace:
    """Lê o número do Control Change informado no terminal."""
    parser = argparse.ArgumentParser(
        description="Testa um Control Change na Matribox II Pro."
    )

    parser.add_argument(
        "control",
        type=int,
        help="Número do Control Change que será testado.",
    )

    return parser.parse_args()


def main() -> None:
    """Envia os valores 127 e 0 para o Control Change escolhido."""
    arguments = parse_arguments()
    control = arguments.control

    if not 0 <= control <= 119:
        raise ValueError(
            "Use somente controles entre 0 e 119 neste teste."
        )

    with MatriboxMidiOutput() as midi_output:
        print(f"Enviando CC {control} com valor 127...")
        midi_output.send_control_change(control, 127)

        time.sleep(TEST_DELAY_SECONDS)

        print(f"Enviando CC {control} com valor 0...")
        midi_output.send_control_change(control, 0)

    print(f"Teste do CC {control} concluído.")


if __name__ == "__main__":
    main()