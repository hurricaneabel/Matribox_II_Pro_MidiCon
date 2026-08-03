"""
Teste manual do recurso Undo/Redo do Looper.

O teste cria uma gravação principal, adiciona uma segunda camada e verifica
se a última camada pode ser desfeita e restaurada.
"""

from __future__ import annotations

import time

from matribox_midi.controller import MatriboxController


RECORDING_TIME = 4
LISTENING_TIME = 5


def main() -> None:
    """Grava uma base, adiciona um overdub e testa Undo/Redo."""
    with MatriboxController() as matribox:
        print("Abrindo o Looper...")
        matribox.looper_on()
        time.sleep(1)

        # Garante que o teste comece sem uma gravação anterior.
        matribox.looper_delete()
        time.sleep(1)

        print("Grave agora a PRIMEIRA parte...")
        matribox.looper_record()
        time.sleep(RECORDING_TIME)
        matribox.looper_stop()

        time.sleep(1)

        print("Iniciando a reprodução da primeira parte...")
        matribox.looper_play()
        time.sleep(1)

        print("Grave agora uma SEGUNDA parte diferente...")
        matribox.looper_record()
        time.sleep(RECORDING_TIME)
        matribox.looper_stop()

        time.sleep(1)

        print("Reproduzindo as duas partes juntas...")
        matribox.looper_play()
        time.sleep(LISTENING_TIME)

        print("Desfazendo a segunda parte...")
        matribox.looper_undo_redo()
        time.sleep(LISTENING_TIME)

        print("Refazendo a segunda parte...")
        matribox.looper_undo_redo()
        time.sleep(LISTENING_TIME)

        print("Parando e fechando o Looper...")
        matribox.looper_stop()
        matribox.looper_off()

    print("Teste concluído.")


if __name__ == "__main__":
    main()