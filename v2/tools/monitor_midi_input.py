"""
Monitor temporário das mensagens MIDI enviadas pela Matribox II Pro.

O programa escuta a porta MIDI de entrada durante 15 segundos.

Os pulsos contínuos de MIDI Clock são contabilizados, mas não são exibidos,
para não encher o terminal e esconder mensagens importantes como SysEx,
Control Change ou Program Change.
"""

from __future__ import annotations

import time

import mido


DEVICE_NAME = "Matribox II Pro"
MONITOR_TIME_SECONDS = 15


def find_matribox_input() -> str:
    """
    Localiza a porta MIDI de entrada da Matribox II Pro.

    Returns:
        Nome completo da porta encontrada.

    Raises:
        RuntimeError:
            Quando nenhuma porta correspondente à Matribox é encontrada.
    """
    for port_name in mido.get_input_names():
        if DEVICE_NAME.casefold() in port_name.casefold():
            return port_name

    raise RuntimeError(
        "A porta MIDI de entrada da Matribox II Pro não foi encontrada."
    )


def format_bytes(message: mido.Message) -> str:
    """
    Converte os bytes da mensagem MIDI para formato hexadecimal.

    Exemplo:
        Uma mensagem SysEx poderá aparecer como:
        F0 21 25 4D 50 ... F7
    """
    return " ".join(f"{byte:02X}" for byte in message.bytes())


def main() -> None:
    """
    Monitora as mensagens MIDI durante um período limitado.

    Mensagens MIDI Clock são ignoradas visualmente porque chegam muitas
    vezes por segundo. Todas as outras mensagens são mostradas no terminal.
    """
    port_name = find_matribox_input()

    received_messages = 0
    clock_messages = 0
    end_time = time.monotonic() + MONITOR_TIME_SECONDS

    print(f"Escutando: {port_name}")
    print(f"O monitor encerrará em {MONITOR_TIME_SECONDS} segundos.")
    print("Marque e desmarque somente o Drum Sync na pedaleira.")
    print("Os pulsos de MIDI Clock não serão exibidos.\n")

    try:
        with mido.open_input(port_name) as input_port:
            while time.monotonic() < end_time:
                for message in input_port.iter_pending():
                    if message.type == "clock":
                        clock_messages += 1
                        continue

                    received_messages += 1

                    print(
                        f"Mensagem: {message} "
                        f"| Bytes: {format_bytes(message)}",
                        flush=True,
                    )

                time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nMonitor interrompido pelo usuário.")

    print()

    if received_messages == 0:
        print("Nenhuma mensagem além do MIDI Clock foi recebida.")
    else:
        print(
            "Total de mensagens diferentes de MIDI Clock: "
            f"{received_messages}"
        )

    print(f"Pulsos de MIDI Clock ignorados: {clock_messages}")
    print("Monitor MIDI encerrado.")


if __name__ == "__main__":
    main()