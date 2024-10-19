import mido

from midimiddleware.components.message_translation_info import MessageTranslationInfo


class MessageTranslator:

    def __init__(self):
        self.translation_infos: dict[tuple, MessageTranslationInfo] = dict()

    def translate(self, message) -> tuple[mido.Message, mido.Message]:
        """
        Returns translated message for [device, virtual]
        """
        address = self._hash_message_address(message)
        if address not in self.translation_infos:
            return  message, message

        if message.type == "control_change":
            return message, mido.Message(
                type='note_on',
                channel=message.channel + 1,
                note=message.control,
                velocity=message.value
            )

    def add_message(self, message: mido.Message):
        self.translation_infos[self._hash_message_address(message)] = MessageTranslationInfo()

    def _hash_message_address(self, message: mido.Message):
        if message.type == "note_on":
            return message.type, message.channel, message.note
        elif message.type == "pitchwheel":
            return message.type, message.channel
        elif message.type == "control_change":
            return message.type, message.channel, message.control
