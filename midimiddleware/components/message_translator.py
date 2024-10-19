from gettext import translation

import mido

from midimiddleware.components.message_translation_info import MessageTranslationInfo


def _hash_message_address(message: mido.Message):
    if message is None:
        return tuple()

    if message.type == "note_on":
        return message.type, message.channel, message.note
    elif message.type == "pitchwheel":
        return message.type, message.channel
    elif message.type == "control_change":
        return message.type, message.channel, message.control


class MessageTranslator:

    def __init__(self):
        self.translation_infos: dict[tuple, MessageTranslationInfo] = dict()

    def reset(self):
        self.translation_infos = dict()

    def get_save_data(self) -> list:
        return [(key, vars(translation)) for key, translation in self.translation_infos.items()]

    def init_with_saved_data(self, data: dict):
        self.translation_infos = {tuple(key): MessageTranslationInfo(**data) for key, data in data}

    def translate(self, message) -> tuple[mido.Message, mido.Message]:
        """
        Returns translated message for [device, virtual]
        """
        address = _hash_message_address(message)
        if address not in self.translation_infos:
            return  message, message

        translation = self.translation_infos[address]
        translated_virtual = mido.Message(
            type=translation.target_type,
            channel=translation.target_channel - 1,
        )
        value = None
        if message.type == "pitchwheel":
            value = message.pitch

        elif message.type == "control_change":
            value = message.value

        elif message.type == "note_on":
            value = message.velocity

        if translation.target_type == "note_on":
            translated_virtual.note = translation.target_index
            translated_virtual.velocity = value

        elif translation.target_type == "control_change":
            translated_virtual.control = translation.target_index
            translated_virtual.value = value

        elif translation.target_type == "pitchwheel":
            translated_virtual.pitch = value

        return message, translated_virtual

    def add_message(self, message: mido.Message):
        channel: int = message.channel
        type_: str = message.type

        if type_ in "note_on":
            index: int = message.note

        elif type_ == "control_change":
            index: int = message.control

        else:
            index: int = -1

        self.translation_infos[_hash_message_address(message)] = MessageTranslationInfo(
            source_channel=channel + 1,
            source_type=type_,
            source_index=index,
            target_channel=channel + 1,
            target_type=type_,
            target_index=index
        )

    def count(self) -> int:
        return len(self.translation_infos)

    def get(self, index: int) -> MessageTranslationInfo:
        return list(self.translation_infos.values())[index]
