"""
Envia rapidamente todos os valores MIDI do CC 61.

O teste começa em 127 e termina em 0 para verificar se algum valor
consegue desativar o Auto Record da Matribox II Pro.
"""

from __future__ import annotations

import time

from matribox_midi import MatriboxMidiOutput


AUTO_RECORD_CC = 61

# 0.02 segundo equivale a 20 milissegundos.
DELAY_SECONDS = 0.50


def main() -> None:
    """Envia os valores de 127 até 0 pelo CC 61."""
    try:
        with MatriboxMidiOutput() as midi_output:
            print(f"Conectado: {midi_output.port_name}")
            print()
            print("Ative o Auto Record manualmente na Matribox.")
            input("Depois pressione Enter para iniciar o teste...")

            print()
            print("Enviando valores de 127 até 0...")

            for value in range(127, -1, -1):
                midi_output.send_control_change(
                    AUTO_RECORD_CC,
                    value,
                )

                print(
                    f"\rCC 61 — valor {value:03d}",
                    end="",
                    flush=True,
                )

                time.sleep(DELAY_SECONDS)

            print()
            print()
            print("Teste concluído.")
            print("Observe se o Auto Record ficou desativado.")

    except RuntimeError as error:
        print(f"Erro de conexão: {error}")


if __name__ == "__main__":
    main()