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

def adjust_volume(controller: MatriboxController) -> None:
    """Solicita e define o volume do preset atual."""
    try:
        volume = int(
            input("Digite o volume, entre 0 e 100: ").strip()
        )
    except ValueError:
        print("Volume inválido. Digite apenas um número.")
        return

    try:
        controller.set_preset_volume(volume)
    except ValueError as error:
        print(f"Erro: {error}")
        return

    print(f"Volume do preset definido para {volume}.")

def define_bpm(controller: MatriboxController) -> None:
    """Solicita e define o BPM do preset atual."""
    try:
        bpm = int(
            input("Digite o BPM, entre 40 e 300: ").strip()
        )
    except ValueError:
        print("BPM inválido. Digite apenas um número.")
        return

    try:
        controller.set_bpm(bpm)
    except ValueError as error:
        print(f"Erro: {error}")
        return

    print(f"BPM definido para {bpm}.")

def control_tuner(controller: MatriboxController) -> None:
    """Permite ligar ou desligar o afinador."""
    print()
    print("=== Afinador ===")
    print("1 - Ligar")
    print("2 - Desligar")
    print("0 - Voltar")

    option = input("Escolha uma opção: ").strip()

    if option == "1":
        controller.tuner_on()
        print("Afinador ligado.")

    elif option == "2":
        controller.tuner_off()
        print("Afinador desligado.")

    elif option == "0":
        return

    else:
        print("Opção inválida.")

def control_quick_access(controller: MatriboxController) -> None:
    """Controla os três knobs Quick Access."""
    print()
    print("=== Quick Access ===")
    print("1 - Definir valor exato")
    print("2 - Aumentar 1 passo")
    print("3 - Diminuir 1 passo")
    print("0 - Voltar")

    action = input("Escolha uma ação: ").strip()

    if action == "0":
        return

    if action not in {"1", "2", "3"}:
        print("Ação inválida.")
        return

    try:
        knob = int(
            input("Escolha o knob, entre 1 e 3: ").strip()
        )
    except ValueError:
        print("Knob inválido. Digite apenas um número.")
        return

    if knob not in (1, 2, 3):
        print("O knob deve ser 1, 2 ou 3.")
        return

    if action == "1":
        try:
            value = int(
                input("Digite o valor, entre 0 e 100: ").strip()
            )
        except ValueError:
            print("Valor inválido. Digite apenas um número.")
            return

        try:
            controller.set_quick_access_knob(knob, value)
        except ValueError as error:
            print(f"Erro: {error}")
            return

        print(f"Knob {knob} definido para {value}.")

    elif action == "2":
        controller.increase_quick_access_knob(knob)
        print(f"Knob {knob} aumentado em 1 passo.")

    else:
        controller.decrease_quick_access_knob(knob)
        print(f"Knob {knob} diminuído em 1 passo.")

def control_drums(controller: MatriboxController) -> None:
    """Controla as principais funções da bateria eletrônica."""
    print()
    print("=== Bateria eletrônica ===")
    print("1 - Abrir menu da bateria")
    print("2 - Fechar menu da bateria")
    print("3 - Iniciar reprodução")
    print("4 - Parar reprodução")
    print("5 - Selecionar ritmo")
    print("6 - Ajustar volume")
    print("0 - Voltar")

    option = input("Escolha uma opção: ").strip()

    if option == "0":
        return

    if option == "1":
        controller.drum_menu_on()
        print("Menu da bateria aberto.")

    elif option == "2":
        controller.drum_menu_off()
        print("Menu da bateria fechado.")

    elif option == "3":
        controller.drum_play()
        print("Bateria iniciada.")

    elif option == "4":
        controller.drum_stop()
        print("Bateria interrompida.")

    elif option == "5":
        try:
            rhythm = int(
                input("Digite o ritmo, entre 0 e 99: ").strip()
            )
            controller.set_drum_rhythm(rhythm)
        except ValueError as error:
            print(f"Erro: {error}")
            return

        print(f"Ritmo da bateria definido para {rhythm}.")

    elif option == "6":
        try:
            volume = int(
                input("Digite o volume, entre 0 e 100: ").strip()
            )
            controller.set_drum_volume(volume)
        except ValueError as error:
            print(f"Erro: {error}")
            return

        print(f"Volume da bateria definido para {volume}.")

    else:
        print("Opção inválida.")

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

                elif option == "1":
                    select_preset(controller)

                elif option == "2":
                    adjust_volume(controller)

                elif option == "3":
                    define_bpm(controller)

                elif option == "4":
                    control_tuner(controller)

                elif option == "5":
                    control_quick_access(controller)

                elif option == "6":
                    control_drums(controller) 

                

                elif option in {"7"}:
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