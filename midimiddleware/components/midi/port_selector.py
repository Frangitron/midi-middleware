import rtmidi
import mido.backends.rtmidi  # this is for PyInstaller


def _sanitize_port_name(name: str) -> str:
    return " ".join(name.split(" ")[:-1])


def _sanitize_port_names(names: list[str]) -> list[str]:
    return sorted([_sanitize_port_name(name) for name in names])


class PortSelector:
    def __init__(self) -> None:
        self._input_ports: list[str] = []
        self._output_ports: list[str] = []

        self.device_in_name = ""
        self.device_out_name = ""
        self.virtual_out_name = ""

    def get_input_ports(self) -> list[str]:
        self._input_ports = _sanitize_port_names(rtmidi.MidiIn().get_ports())
        return self._input_ports

    def get_output_ports(self) -> list[str]:
        self._output_ports = _sanitize_port_names(rtmidi.MidiOut().get_ports())
        return self._output_ports

    def select_ports(self, device_in, device_out, virtual_out) -> None:
        self.device_in_name = device_in
        self.device_out_name = device_out
        self.virtual_out_name = virtual_out

    def reset(self):
        self.device_in_name = ""
        self.device_out_name = ""
        self.virtual_out_name = ""

    def get_save_data(self) -> dict:
        return {
            "device_in": self.device_in_name,
            "device_out": self.device_out_name,
            "virtual_out": self.virtual_out_name
        }

    def init_with_saved_data(self, data: dict):
        """
        Reloads port lists and apply saved port selection (if ports are still available)
        """
        self.get_input_ports()
        self.get_output_ports()

        if data["device_in"] not in self._input_ports:
            data["device_in"] = ""

        if data["device_out"] not in self._output_ports:
            data["device_out"] = ""

        if data["virtual_out"] not in self._output_ports:
            data["virtual_out"] = ""

        self.select_ports(
            device_in=data["device_in"],
            device_out=data["device_out"],
            virtual_out=data["virtual_out"]
        )
