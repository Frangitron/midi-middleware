import mido


class Translator:

    def __init__(self):
        self.translations: dict[tuple, bool] = dict()

    def translate(self, message) -> tuple[mido.Message, mido.Message]:
        """
        Returns translated message for [device, virtual]
        """
        if message.type == "control_change":
            return message, mido.Message(
                type='note_on',
                channel=message.channel + 1,
                note=message.control,
                velocity=message.value
            )

        address = self._hash_message_address(message)
        if address not in self.translations:
            return  message, message

        # TODO translate

    def _hash_message_address(self, message: mido.Message):
        if message.type == "note_on":
            return message.type, message.channel, message.note
        elif message.type == "pitchwheel":
            return message.type, message.channel
        elif message.type == "control_change":
            return message.type, message.channel, message.control
