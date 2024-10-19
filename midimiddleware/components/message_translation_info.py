from dataclasses import dataclass


@dataclass
class MessageTranslationInfo:
    source_channel: int
    source_type: str
    source_index: int

    target_channel: int
    target_type: str
    target_index: int

    is_toggle: bool = False
