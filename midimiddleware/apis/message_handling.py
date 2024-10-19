import mido

from midimiddleware.components.components import Components
from midimiddleware.components_ui.components_ui import ComponentsUi


def handle_message(message: mido.Message):
    # TODO check if this is always legit
    if message.type == 'note_off':
        message = mido.Message('note_on', note=message.note, velocity=0)

    translated_message = Components().translator.translate(message)
    loopback_message = Components().translator.make_loopback(message)
    Components().devices.send_messages(device=loopback_message, virtual=translated_message)

    ComponentsUi().monitor.set_messages(
        device_in=message,
        device_out=loopback_message if Components().devices.has_device_out() else None,
        virtual_out=translated_message if Components().devices.has_virtual_out() else None
    )
    ComponentsUi().table.select_translation_from_message(message)
