import mido
from matribox_sysex import decode_sysex

PORT_NAME = "Matribox II Pro Subdevice 0"

# Mostrar apenas mensagens potencialmente interessantes
MIN_LENGTH = 80


def print_sysex(data):
    if len(data) < MIN_LENGTH:
        return

    decoded = decode_sysex(data)

    print()
    print("=" * 80)
    print(f"LEN    : {len(data)}")
    print(f"EVENT  : {data[6] if len(data) > 6 else None}")
    print(f"DATA8  : {data[8] if len(data) > 8 else None}")
    print(f"DECODE : {decoded}")

    print("RAW:")
    print(data)


with mido.open_input(PORT_NAME) as port:
    print(f"Reverse listener rodando em: {PORT_NAME}")
    print(f"Mostrando apenas mensagens LEN >= {MIN_LENGTH}")
    print("Pressione CTRL+C para sair.")

    try:
        for msg in port:

            if msg.type != "sysex":
                continue

            data = list(msg.data)

            print_sysex(data)

    except KeyboardInterrupt:
        print()
        print("Reverse listener encerrado.")