import mido

from midimiddleware.components.components import Components
from midimiddleware.components.midi.devices import Devices
from midimiddleware.components_ui.components_ui import ComponentsUi



class Engine:
    def __init__(self):
        self._devices = Devices(message_in_callback=self._handle_device_in)

    def start(self):
        self._devices.open_ports()

    def stop(self):
        self._devices.close_ports()

    def _handle_device_in(self, message: mido.Message):
        translated_device, translated_virtual = Components().translator.translate(message)
        self._devices.send_messages(device=translated_device, virtual=translated_virtual)

        ComponentsUi().monitor.set_messages(
            device_in=message,
            device_out=translated_device if self._devices.has_device_out() else None,
            virtual_out=translated_virtual if self._devices.has_virtual_out() else None
        )
