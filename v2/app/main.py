"""
Aplicativo de terminal para controlar a Matribox II Pro.

Este aplicativo permite testar as funções MIDI da biblioteca antes da
criação da interface gráfica definitiva.
"""

from __future__ import annotations

from matribox_midi import MatriboxController
from matribox_midi.drum_rhythms import DRUM_RHYTHMS


def show_main_menu() -> None:
    """Exibe as opções principais do aplicativo."""
    print()
    print("=== Matribox II Pro MIDI Controller ===")
    print("1 - Selecionar preset")
    print("2 - Ajustar volume")
    print("3 - Definir BPM do preset")
    print("4 - Controlar afinador")
    print("5 - Controlar Quick Access")
    print("6 - Controlar bateria")
    print("7 - Controlar Looper")
    print("0 - Sair")


def select_preset(controller: MatriboxController) -> None:
    """Solicita o banco e a letra do preset."""
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

    print(f"BPM do preset definido para {bpm}.")


def control_tuner(controller: MatriboxController) -> None:
    """Permite ligar ou desligar o afinador."""
    print()
    print("=== Afinador ===")
    print("1 - Ligar")
    print("2 - Desligar")
    print("0 - Voltar")

    option = input("Escolha uma opção: ").strip()

    if option == "0":
        return

    elif option == "1":
        controller.tuner_on()
        print("Afinador ligado.")

    elif option == "2":
        controller.tuner_off()
        print("Afinador desligado.")

    else:
        print("Opção inválida.")


def control_quick_access(
    controller: MatriboxController,
) -> None:
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
                input(
                    "Digite o valor, entre 0 e 100: "
                ).strip()
            )
        except ValueError:
            print("Valor inválido. Digite apenas um número.")
            return

        try:
            controller.set_quick_access_knob(
                knob,
                value,
            )
        except ValueError as error:
            print(f"Erro: {error}")
            return

        print(f"Knob {knob} definido para {value}.")

    elif action == "2":
        controller.increase_quick_access_knob(knob)
        print(f"Knob {knob} aumentado em 1 passo.")

    elif action == "3":
        controller.decrease_quick_access_knob(knob)
        print(f"Knob {knob} diminuído em 1 passo.")


def control_drums(controller: MatriboxController) -> None:
    """Controla as funções da bateria eletrônica."""
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

    elif option == "1":
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
        print()
        print("=== Ritmos disponíveis ===")

        for rhythm_number, rhythm_name in DRUM_RHYTHMS.items():
            print(
                f"{rhythm_number:02d} - {rhythm_name}"
            )

        try:
            rhythm = int(
                input(
                    "Digite o número do ritmo: "
                ).strip()
            )

            controller.set_drum_rhythm(rhythm)

        except ValueError as error:
            print(f"Erro: {error}")
            return

        rhythm_name = DRUM_RHYTHMS[rhythm]

        print(
            f"Ritmo selecionado: "
            f"{rhythm:02d} - {rhythm_name}."
        )

    elif option == "6":
        try:
            volume = int(
                input(
                    "Digite o volume, entre 0 e 100: "
                ).strip()
            )

            controller.set_drum_volume(volume)

        except ValueError as error:
            print(f"Erro: {error}")
            return

        print(
            f"Volume da bateria definido para {volume}."
        )

    else:
        print("Opção inválida.")


def control_looper(controller: MatriboxController) -> None:
    """Controla as principais funções do Looper."""
    while True:
        print()
        print("=== Looper ===")
        print("1 - Abrir Looper")
        print("2 - Fechar Looper")
        print("3 - Iniciar gravação")
        print("4 - Preparar gravação automática")
        print("5 - Reproduzir")
        print("6 - Parar")
        print("7 - Desfazer ou refazer overdub")
        print("8 - Apagar gravação")
        print("9 - Ajustar volume de gravação")
        print("10 - Ajustar volume de reprodução")
        print("11 - Posicionar Looper antes dos efeitos — Pre")
        print("12 - Posicionar Looper depois dos efeitos — Post")
        print("0 - Voltar")

        option = input("Escolha uma opção: ").strip()

        if option == "0":
            return

        elif option == "1":
            controller.looper_on()
            print("Looper aberto.")

        elif option == "2":
            controller.looper_off()
            print("Looper fechado.")

        elif option == "3":
            controller.looper_record()
            print("Gravação iniciada.")

        elif option == "4":
            controller.looper_auto_record()
            print(
                "Gravação automática preparada. "
                "Ela começará quando houver sinal do instrumento."
            )

        elif option == "5":
            controller.looper_play()
            print("Reprodução iniciada.")

        elif option == "6":
            controller.looper_stop()
            print("Looper interrompido.")

        elif option == "7":
            controller.looper_undo_redo()
            print("Comando de desfazer/refazer enviado.")

        elif option == "8":
            confirmation = input(
                "Apagar a gravação atual? "
                "Digite S para confirmar: "
            ).strip().upper()

            if confirmation == "S":
                controller.looper_delete()
                print("Gravação apagada.")
            else:
                print("Exclusão cancelada.")

        elif option == "9":
            try:
                volume = int(
                    input(
                        "Digite o volume de gravação, "
                        "entre 0 e 100: "
                    ).strip()
                )

                controller.set_looper_recording_volume(volume)

            except ValueError as error:
                print(f"Erro: {error}")
                continue

            print(
                f"Volume de gravação definido para {volume}."
            )

        elif option == "10":
            try:
                volume = int(
                    input(
                        "Digite o volume de reprodução, "
                        "entre 0 e 100: "
                    ).strip()
                )

                controller.set_looper_playback_volume(volume)

            except ValueError as error:
                print(f"Erro: {error}")
                continue

            print(
                f"Volume de reprodução definido para {volume}."
            )

        elif option == "11":
            controller.set_looper_pre()
            print(
                "Looper posicionado antes da cadeia de efeitos — Pre."
            )

        elif option == "12":
            controller.set_looper_post()
            print(
                "Looper posicionado depois da cadeia de efeitos — Post."
            )

        else:
            print("Opção inválida.")

def main() -> None:
    """Conecta à Matribox e executa o menu principal."""
    try:
        with MatriboxController() as controller:
            print(
                f"Conectado à porta MIDI: "
                f"{controller.port_name}"
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

                elif option == "7":
                    control_looper(controller)

                else:
                    print(
                        "Opção inválida. "
                        "Escolha um número entre 0 e 7."
                    )

    except RuntimeError as error:
        print(f"Não foi possível conectar: {error}")


if __name__ == "__main__":
    main()