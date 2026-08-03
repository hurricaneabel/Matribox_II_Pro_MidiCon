"""
Utilitário para listar as portas MIDI de saída disponíveis.

Este arquivo não envia nenhum comando para a pedaleira.
Ele serve apenas para confirmar se o sistema operacional e o Python
conseguem reconhecer dispositivos MIDI conectados.
"""

from __future__ import annotations

import mido


def get_output_ports() -> list[str]:
    """
    Retorna os nomes de todas as portas MIDI de saída encontradas.

    Returns:
        Uma lista contendo o nome de cada porta MIDI disponível.
        A lista será vazia caso nenhuma porta seja encontrada.
    """
    return list(mido.get_output_names())


def main() -> None:
    """Executa a listagem das portas MIDI no terminal."""
    output_ports = get_output_ports()

    print("Portas MIDI de saída encontradas:")

    if not output_ports:
        print("- Nenhuma porta MIDI foi encontrada.")
        return

    for position, port_name in enumerate(output_ports, start=1):
        print(f"{position}. {port_name}")


if __name__ == "__main__":
    main()