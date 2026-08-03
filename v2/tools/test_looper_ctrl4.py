"""
Testa o footswitch CTRL 4 com a tela do Looper aberta.

Um toque curto deve executar a função normal do CTRL 4.
Um toque longo deve simular o footswitch sendo segurado.
"""

from __future__ import annotations

import time

from matribox_midi import MatriboxController, StompControl


SHORT_PRESS_SECONDS = 0.10
LONG_PRESS_SECONDS = 2.0


def press_ctrl4(
    controller: MatriboxController,
    duration: float,
) -> None:
    """
    Pressiona o CTRL 4, aguarda e depois libera.

    Args:
        controller:
            Controlador conectado à Matribox.

        duration:
            Tempo em segundos durante o qual o CTRL 4 ficará pressionado.
    """
    print("CTRL 4 pressionado.")

    controller.stomp_control_on(
        StompControl.CONTROL_4,
    )

    time.sleep(duration)

    controller.stomp_control_off(
        StompControl.CONTROL_4,
    )

    print("CTRL 4 liberado.")


def main() -> None:
    """Executa o teste interativo do CTRL 4."""
    try:
        with MatriboxController() as controller:
            print(f"Conectado: {controller.port_name}")
            print()
            print("Abra a tela do Looper na Matribox.")
            print()
            print("1 - Toque curto no CTRL 4")
            print("2 - Segurar CTRL 4 por 2 segundos")
            print("0 - Sair")

            while True:
                option = input("Escolha uma opção: ").strip()

                if option == "0":
                    break

                elif option == "1":
                    press_ctrl4(
                        controller,
                        SHORT_PRESS_SECONDS,
                    )

                elif option == "2":
                    press_ctrl4(
                        controller,
                        LONG_PRESS_SECONDS,
                    )

                else:
                    print("Opção inválida.")

    except RuntimeError as error:
        print(f"Erro de conexão: {error}")


if __name__ == "__main__":
    main()