"""
Envia um pedido universal de identificação SysEx para a Matribox
e captura todas as mensagens MIDI recebidas.

O arquivo também abre uma etapa de captura manual para observar
se ações realizadas fisicamente na pedaleira geram mensagens MIDI.
"""

from __future__ import annotations

import time
from pathlib import Path

import mido
from mido.backends.backend import Backend


INPUT_PORT_HINT = "Matribox II Pro Subdevice 0"
OUTPUT_PORT_HINT = "Matribox II Pro Subdevice 1"
MIDI_BACKEND = Backend("mido.backends.rtmidi")

IDENTITY_CAPTURE_SECONDS = 5
MANUAL_CAPTURE_SECONDS = 30

LOG_FILE = Path(__file__).with_name(
    "matribox_sysex_capture.txt"
)


def find_port(
    available_ports: list[str],
    expected_name: str,
) -> str:
    """Localiza uma porta MIDI da Matribox."""
    if expected_name in available_ports:
        return expected_name

    for port_name in available_ports:
        if "Matribox II Pro" in port_name:
            return port_name

    raise RuntimeError(
        f"Porta não encontrada: {expected_name}"
    )


def clear_pending_messages(
    input_port: mido.ports.BaseInput,
) -> None:
    """Remove mensagens antigas que estavam aguardando leitura."""
    while input_port.poll() is not None:
        pass


def capture_messages(
    input_port: mido.ports.BaseInput,
    duration: float,
    log_file,
) -> int:
    """
    Captura mensagens MIDI durante o período informado.

    Retorna a quantidade de mensagens SysEx encontradas.
    """
    sysex_count = 0
    start_time = time.monotonic()
    end_time = start_time + duration

    while time.monotonic() < end_time:
        message = input_port.poll()

        if message is None:
            time.sleep(0.005)
            continue

        # Ignora MIDI Clock para não poluir o resultado.
        if message.type == "clock":
            continue

        elapsed = time.monotonic() - start_time

        line = (
            f"{elapsed:08.3f}s | "
            f"{message.hex()} | "
            f"{message}"
        )

        print(line)
        log_file.write(line + "\n")
        log_file.flush()

        if message.type == "sysex":
            sysex_count += 1
            print(">>> MENSAGEM SYSEX ENCONTRADA <<<")

    return sysex_count


def main() -> None:
    """Executa o pedido de identidade e a captura manual."""
    input_ports = MIDI_BACKEND.get_input_names()
    output_ports = MIDI_BACKEND.get_output_names()

    print("Portas MIDI de entrada:")
    for port_name in input_ports:
        print(f"  {port_name}")

    print()
    print("Portas MIDI de saída:")
    for port_name in output_ports:
        print(f"  {port_name}")

    try:
        input_name = find_port(
            input_ports,
            INPUT_PORT_HINT,
        )

        output_name = find_port(
            output_ports,
            OUTPUT_PORT_HINT,
        )

    except RuntimeError as error:
        print()
        print(f"Erro: {error}")
        return

    try:
        with (
            MIDI_BACKEND.open_input(input_name) as input_port,
            MIDI_BACKEND.open_output(output_name) as output_port,
            LOG_FILE.open(
                "w",
                encoding="utf-8",
            ) as log_file,
        ):
            print()
            print(f"Entrada aberta: {input_name}")
            print(f"Saída aberta: {output_name}")

            clear_pending_messages(input_port)

            # O Mido acrescenta F0 e F7 automaticamente.
            # Mensagem completa:
            # F0 7E 7F 06 01 F7
            identity_request = mido.Message(
                "sysex",
                data=[
                    0x7E,
                    0x7F,
                    0x06,
                    0x01,
                ],
            )

            print()
            print(
                "Enviando pedido universal de identificação:"
            )
            print(identity_request.hex())

            output_port.send(identity_request)

            identity_sysex_count = capture_messages(
                input_port,
                IDENTITY_CAPTURE_SECONDS,
                log_file,
            )

            print()
            print("=== Captura manual ===")
            print(
                "Durante os próximos 30 segundos, faça:"
            )
            print("1. Abra o Looper.")
            print("2. Pressione CTRL 4 rapidamente.")
            print("3. Segure CTRL 4.")
            print("4. Ative ou desative Auto Record.")
            print("5. Ative ou desative Drum Sync.")

            input(
                "Pressione Enter quando estiver preparado..."
            )

            clear_pending_messages(input_port)

            manual_sysex_count = capture_messages(
                input_port,
                MANUAL_CAPTURE_SECONDS,
                log_file,
            )

    except OSError as error:
        print(f"Erro ao abrir a porta MIDI: {error}")
        return

    total_sysex = (
        identity_sysex_count
        + manual_sysex_count
    )

    print()
    print("=== Resultado ===")
    print(f"Mensagens SysEx encontradas: {total_sysex}")
    print(f"Log salvo em: {LOG_FILE}")

    if total_sysex == 0:
        print(
            "A Matribox não enviou SysEx por essa porta "
            "durante o teste."
        )


if __name__ == "__main__":
    main()