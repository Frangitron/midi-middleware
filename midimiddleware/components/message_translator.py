from copy import copy

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
        self._toggle_states: dict[tuple, bool] = dict()

    def reset(self):
        self.translation_infos = dict()

    def get_save_data(self) -> list:
        return [(key, vars(translation)) for key, translation in self.translation_infos.items()]

    def init_with_saved_data(self, data: dict):
        self.translation_infos = {tuple(key): MessageTranslationInfo(**data) for key, data in data}

    def translate(self, message) -> mido.Message:
        """
        Returns translated message for [device, virtual]
        """
        #
        # Get translation
        address = _hash_message_address(message)
        translation = self.translation_infos.get(address, None)
        if translation is None:
            return  message

        translated_message = mido.Message(
            type=translation.target_type,
            channel=translation.target_channel - 1,
        )

        #
        # Get value
        value = None

        if message.type == "pitchwheel":
            value = int(((message.pitch + 8192.0) / 16380.0) * 127.0)

        elif message.type == "control_change":
            value = message.value

        elif message.type == "note_on":
            value = message.velocity

        #
        # Get toggle
        if translation.is_toggle:
            if value < 64:
                return None

            if address not in self._toggle_states:
                self._toggle_states[address] = False

            self._toggle_states[address] = not self._toggle_states[address]
            value = 127 if self._toggle_states[address] else 0

        if translation.target_type == "note_on":
            if 0 >= translation.target_index >= 127:
                raise ValueError(f"Note index is out of range: {translation.target_index} (0-127)")

            translated_message.note = translation.target_index
            translated_message.velocity = value

        elif translation.target_type == "control_change":
            translated_message.control = translation.target_index
            translated_message.value = value

        elif translation.target_type == "pitchwheel":
            translated_message.pitch = int(((value / 127.0) * 16380.0) - 8192.0)

        return translated_message

    def make_loopback(self, message: mido.Message):
        #
        # Get translation
        address = _hash_message_address(message)
        translation = self.translation_infos.get(address, None)

        loopback_message = copy(message)

        #
        # Get value
        value = None

        if message.type == "pitchwheel":
            value = int(((message.pitch + 8192.0) / 16380.0) * 127.0)

        elif message.type == "control_change":
            value = message.value

        elif message.type == "note_on":
            value = message.velocity

        #
        # Get toggle
        if message.type == "note_on":
            if translation is not None and translation.is_toggle :
                if value < 64:
                    return None

                loopback_message.velocity = self._toggle_states[address] * 127

            # FIXME !! Akai APCmini 2 specific, use device profile !!
            if message.note <= 63:
                loopback_message.velocity = 91 if loopback_message.velocity else 0

        return loopback_message

    def add_message(self, message: mido.Message):
        channel: int = message.channel
        type_: str = message.type

        if type_ in "note_on":
            index: int = message.note

        elif type_ == "control_change":
            index: int = message.control

        else:
            index: int = None

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
