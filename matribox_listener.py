import threading
import mido

from matribox_sysex import decode_sysex


class MatriboxListener:
    def __init__(self, input_port_name, state=None):
        self.input_port_name = input_port_name
        self.state = state
        self.running = False
        self.thread = None

    def start(self):
        if self.running:
            return

        self.running = True
        self.thread = threading.Thread(target=self._listen, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False

    def _listen(self):
        with mido.open_input(self.input_port_name) as port:
            print(f"Listener iniciado em: {self.input_port_name}")

            while self.running:
                for msg in port.iter_pending():
                    self._handle_message(msg)

    def _handle_message(self, msg):
        if msg.type != "sysex":
            return

        data = list(msg.data)
        decoded = decode_sysex(data)

        print("SYSEX:", decoded)

        if self.state is not None:
            self._update_state(decoded)

    def _update_state(self, decoded):
        msg_type = decoded.get("type")

        if msg_type == "preset":
            self.state.set_preset(decoded["bank"], decoded["letter"])

        elif msg_type == "mode":
            self.state.set_mode(decoded["mode"])

        elif msg_type == "effect_block":
            self.state.set_module(decoded["slot"], decoded["enabled"])

        elif msg_type == "drum":
            self.state.set_drum_playing(decoded["playing"])