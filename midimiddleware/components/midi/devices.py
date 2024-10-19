from typing import Callable
import mido

from midimiddleware.components.components import Components
from midimiddleware.python_extensions.traceback_print_wrapper import traceback_print_wrapper


class Devices:
    def __init__(self, message_in_callback: Callable[[mido.Message], None]):
        self._device_in: mido.ports.BaseInput = None
        self._device_out: mido.ports.BaseOutput = None
        self._virtual_out: mido.ports.BaseOutput = None
        self._message_in_callback = message_in_callback

    def send_message(self, device, virtual):
        if self._device_out is not None:
            self._device_out.send(device)

        if self._virtual_out is not None:
            self._virtual_out.send(virtual)

    def open_ports(self):
        self.close_ports()
        port_selector = Components().port_selector
        print(f"Opening ports: "
              f"device='{port_selector.device_in_name}', "
              f"'{port_selector.device_out_name}', "
              f"virtual='{port_selector.virtual_out_name}'"
        )

        if port_selector.device_in_name:
            self._device_in = mido.open_input(
                port_selector.device_in_name,
                callback=traceback_print_wrapper(self._message_in_callback)
            )

        if port_selector.device_out_name:
            self._device_out = mido.open_output(port_selector.device_out_name)

        if port_selector.virtual_out_name:
            self._virtual_out = mido.open_output(port_selector.virtual_out_name)

    def close_ports(self):
        print(f"Closing ports")

        if self._device_in:
            self._device_in.close()
            self._device_in = None

        if self._device_out:
            self._device_out.close()
            self._device_out = None

        if self._virtual_out:
            self._virtual_out.close()
            self._virtual_out = None

    def has_device_out(self) -> bool:
        return self._device_out is not None

    def has_virtual_out(self) -> bool:
        return self._virtual_out is not None
