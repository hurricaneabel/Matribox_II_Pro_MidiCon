import tkinter as tk
import mido

PORTA = "Matribox II Pro Subdevice 1"
out = mido.open_output(PORTA)


def enviar_cc(cc, valor=127):
    out.send(
        mido.Message(
            "control_change",
            channel=0,
            control=cc,
            value=valor
        )
    )


janela = tk.Tk()
janela.title("Matribox Controller")
janela.geometry("400x300")


tk.Button(
    janela,
    text="Preset +",
    width=20,
    height=2,
    command=lambda: enviar_cc(24)
).pack(pady=5)

tk.Button(
    janela,
    text="Preset -",
    width=20,
    height=2,
    command=lambda: enviar_cc(25)
).pack(pady=5)

tk.Button(
    janela,
    text="Bank +",
    width=20,
    height=2,
    command=lambda: enviar_cc(22)
).pack(pady=5)

tk.Button(
    janela,
    text="Bank -",
    width=20,
    height=2,
    command=lambda: enviar_cc(23)
).pack(pady=5)

tk.Button(
    janela,
    text="Afinador ON",
    width=20,
    height=2,
    command=lambda: enviar_cc(58, 127)
).pack(pady=5)

tk.Button(
    janela,
    text="Afinador OFF",
    width=20,
    height=2,
    command=lambda: enviar_cc(58, 0)
).pack(pady=5)

janela.mainloop()