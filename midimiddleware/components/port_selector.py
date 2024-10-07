import rtmidi


class PortSelector:
    def __init__(self) -> None:
        self._input_ports: list[str] = []
        self._output_ports: list[str] = []

        self.device_in_name = ""
        self.device_out_name = ""
        self.virtual_in_name = ""
        self.virtual_out_name = ""

        self.device_in: rtmidi.MidiIn = None
        self.device_out: rtmidi.MidiOut = None
        self.virtual_in: rtmidi.MidiIn = None
        self.virtual_out: rtmidi.MidiOut = None

    def get_input_ports(self) -> list[str]:
        self._input_ports = rtmidi.MidiIn().get_ports()
        return self._input_ports

    def get_output_ports(self) -> list[str]:
        self._output_ports = rtmidi.MidiOut().get_ports()
        return self._output_ports

    def select_ports(self, device_in, device_out, virtual_in, virtual_out) -> None:
        self.device_in_name = device_in
        self.device_out_name = device_out
        self.virtual_in_name = virtual_in
        self.virtual_out_name = virtual_out

        self.open()

    def open(self):
        self.close()
        self.device_in = rtmidi.MidiIn().open_port(self._input_ports.index(self.device_in_name))
        self.device_out = rtmidi.MidiOut().open_port(self._output_ports.index(self.device_out_name))
        self.virtual_in = rtmidi.MidiIn().open_port(self._input_ports.index(self.virtual_in_name))
        self.virtual_out = rtmidi.MidiOut().open_port(self._output_ports.index(self.virtual_out_name))

    def close(self):
        if self.device_in:
            self.device_in.close_port()
            self.device_in = None
        if self.device_out:
            self.device_out.close_port()
            self.device_out = None
        if self.virtual_in:
            self.virtual_in.close_port()
            self.virtual_in = None
        if self.virtual_out:
            self.virtual_out.close_port()
            self.virtual_out = None
