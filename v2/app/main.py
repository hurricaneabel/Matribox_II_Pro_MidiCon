"""
Aplicativo de terminal para controlar a Matribox II Pro.

Nesta etapa, a seleção direta de presets já funciona por MIDI.
As demais opções serão conectadas gradualmente.
"""

from __future__ import annotations

from matribox_midi import MatriboxController


def show_main_menu() -> None:
    """Exibe as opções principais do aplicativo."""
    print()
    print("=== Matribox II Pro MIDI Controller ===")
    print("1 - Selecionar preset")
    print("2 - Ajustar volume")
    print("3 - Definir BPM")
    print("4 - Controlar afinador")
    print("5 - Controlar Quick Access")
    print("6 - Controlar bateria")
    print("7 - Controlar Looper")
    print("0 - Sair")


def select_preset(controller: MatriboxController) -> None:
    """Solicita banco e letra e seleciona o preset na Matribox."""
    try:
        bank = int(
            input("Digite o banco, entre 1 e 60: ").strip()
        )
    except ValueError:
        print("Banco inválido. Digite apenas um número.")
        return

    preset = input(
        "Digite a letra do preset, A, B, C ou D: "
    ).strip()

    try:
        controller.select_preset(bank, preset)
    except ValueError as error:
        print(f"Erro: {error}")
        return

    print(
        f"Preset {bank:02d}{preset.upper()} selecionado."
    )


def main() -> None:
    """Conecta à Matribox e executa o menu principal."""
    try:
        with MatriboxController() as controller:
            print(
                f"Conectado à porta MIDI: {controller.port_name}"
            )

            while True:
                show_main_menu()

                option = input(
                    "Escolha uma opção: "
                ).strip()

                if option == "0":
                    print("Aplicativo encerrado.")
                    break

                if option == "1":
                    select_preset(controller)

                elif option in {"2", "3", "4", "5", "6", "7"}:
                    print(
                        "Essa opção será conectada "
                        "nas próximas etapas."
                    )

                else:
                    print(
                        "Opção inválida. "
                        "Escolha um número entre 0 e 7."
                    )

    except RuntimeError as error:
        print(f"Não foi possível conectar: {error}")


if __name__ == "__main__":
    main()