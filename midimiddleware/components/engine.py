import mido

from midimiddleware.components.components import Components
from midimiddleware.python_extensions.traceback_print_wrapper import traceback_print_wrapper
from midimiddleware.ui_components.ui_components import UiComponents


def hash_message_address(message: mido.Message):
    if message.type == "note_on":
        return message.type, message.channel, message.note
    elif message.type == "pitchwheel":
        return message.type, message.channel
    elif message.type == "control_change":
        return message.type, message.channel, message.control


class Engine:
    def __init__(self):
        self._device_in: mido.ports.BaseInput = None
        self._device_out: mido.ports.BaseOutput = None
        self._virtual_in: mido.ports.BaseInput = None
        self._virtual_out: mido.ports.BaseOutput = None

        self.translations: dict[tuple, bool] = dict()

    def start(self):
        self._open_ports()

    def stop(self):
        self._close_ports()

    def _handle_device_in(self, message, _=None):
        UiComponents().monitor.set_message(message)

        address = hash_message_address(message)
        if address not in self.translations:
            if self._device_out is not None:
                self._device_out.send(message)
            if self._virtual_out is not None:
                self._virtual_out.send(message)
            return

        translated_device, translated_virtual = self.translations[address].translate(message)
        if self._device_out is not None:
            self._device_out.send(translated_device)
        if self._virtual_out is not None:
            self._virtual_out.send(translated_virtual)

    def _open_ports(self):
        self._close_ports()
        port_selector = Components().port_selector
        print(f"Opening ports: "
              f"{port_selector.device_in_name}, "
              f"{port_selector.device_out_name}, "
              f"{port_selector.virtual_in_name}, "
              f"{port_selector.virtual_out_name}"
        )
        if port_selector.device_in_name:
            self._device_in = mido.open_input(port_selector.device_in_name, callback=traceback_print_wrapper(self._handle_device_in))
        if port_selector.device_out_name:
            self._device_out = mido.open_output(port_selector.device_out_name)
        if port_selector.virtual_in_name:
            self._virtual_in = mido.open_input(port_selector.virtual_in_name)
        if port_selector.virtual_out_name:
            self._virtual_out = mido.open_output(port_selector.virtual_out_name)

    def _close_ports(self):
        print(f"Closing ports")
        if self._device_in:
            self._device_in.close()
            self._device_in = None
        if self._device_out:
            self._device_out.close()
            self._device_out = None
        if self._virtual_in:
            self._virtual_in.close()
            self._virtual_in = None
        if self._virtual_out:
            self._virtual_out.close()
            self._virtual_out = None
