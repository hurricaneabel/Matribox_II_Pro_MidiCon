"""
Monitor temporário das mensagens MIDI enviadas pela Matribox II Pro.

O programa escuta a porta MIDI de entrada durante 15 segundos e exibe
qualquer mensagem recebida. Depois desse período, encerra automaticamente.
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
            Quando nenhuma porta correspondente é encontrada.
    """
    for port_name in mido.get_input_names():
        if DEVICE_NAME.casefold() in port_name.casefold():
            return port_name

    raise RuntimeError(
        "A porta MIDI de entrada da Matribox II Pro não foi encontrada."
    )


def format_bytes(message: mido.Message) -> str:
    """Converte os bytes MIDI para representação hexadecimal."""
    return " ".join(f"{byte:02X}" for byte in message.bytes())


def main() -> None:
    """Monitora as mensagens MIDI por um período limitado."""
    port_name = find_matribox_input()
    received_messages = 0
    end_time = time.monotonic() + MONITOR_TIME_SECONDS

    print(f"Escutando: {port_name}")
    print(f"O monitor encerrará em {MONITOR_TIME_SECONDS} segundos.")
    print("Agora marque e desmarque o Drum Sync na pedaleira.\n")

    with mido.open_input(port_name) as input_port:
        while time.monotonic() < end_time:
            for message in input_port.iter_pending():
                received_messages += 1

                print(
                    f"Mensagem: {message} "
                    f"| Bytes: {format_bytes(message)}",
                    flush=True,
                )

            time.sleep(0.01)

    if received_messages == 0:
        print("Nenhuma mensagem MIDI foi recebida.")
    else:
        print(f"\nTotal de mensagens recebidas: {received_messages}")

    print("Monitor MIDI encerrado automaticamente.")


if __name__ == "__main__":
    main()