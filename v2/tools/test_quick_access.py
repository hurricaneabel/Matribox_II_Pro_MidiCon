"""
Testa os três knobs Quick Access da Matribox II Pro.

Exemplos:
    python v2/tools/test_quick_access.py 1 set 50
    python v2/tools/test_quick_access.py 1 increase
    python v2/tools/test_quick_access.py 1 decrease
"""

from __future__ import annotations

import argparse

from matribox_midi.controller import MatriboxController


def main() -> None:
    """Executa uma ação em um dos knobs Quick Access."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "knob",
        type=int,
        choices=(1, 2, 3),
        help="Número do knob Quick Access.",
    )

    parser.add_argument(
        "action",
        choices=("set", "increase", "decrease"),
        help="Ação que será executada.",
    )

    parser.add_argument(
        "value",
        type=int,
        nargs="?",
        help="Valor entre 0 e 100, usado somente na ação set.",
    )

    arguments = parser.parse_args()

    if arguments.action == "set" and arguments.value is None:
        parser.error("A ação set precisa de um valor entre 0 e 100.")

    with MatriboxController() as controller:
        if arguments.action == "set":
            controller.set_quick_access_knob(
                arguments.knob,
                arguments.value,
            )

            print(
                f"Knob {arguments.knob} definido para "
                f"{arguments.value}."
            )

        elif arguments.action == "increase":
            controller.increase_quick_access_knob(arguments.knob)

            print(
                f"Knob {arguments.knob} aumentado em 1 passo."
            )

        else:
            controller.decrease_quick_access_knob(arguments.knob)

            print(
                f"Knob {arguments.knob} diminuído em 1 passo."
            )


if __name__ == "__main__":
    main()