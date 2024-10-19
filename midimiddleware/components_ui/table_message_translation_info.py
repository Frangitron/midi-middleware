from dataclasses import dataclass

from PySide6.QtWidgets import QStyledItemDelegate

from pyside6helpers.item_delegates import BooleanDelegate, IntegerDelegate, ListDelegate


class AttributeUiInfo:
    def __init__(self, caption: str, editable: bool = False, delegate: QStyledItemDelegate | None = None):
        self.caption = caption
        self.editable = editable
        self.delegate = delegate


@dataclass
class TableMessageTranslationInfo:
    source_channel: AttributeUiInfo = AttributeUiInfo("Channel")
    source_type: AttributeUiInfo = AttributeUiInfo("Type")
    source_index: AttributeUiInfo = AttributeUiInfo("Index")

    target_channel: AttributeUiInfo = AttributeUiInfo("Target channel", editable=True, delegate=IntegerDelegate())
    target_type: AttributeUiInfo = AttributeUiInfo("Target type", editable=True, delegate=ListDelegate([
        'note_on', 'control_change', 'pitchwheel'
    ]))
    target_index: AttributeUiInfo = AttributeUiInfo("Target index", editable=True)

    is_toggle: AttributeUiInfo = AttributeUiInfo("Toggle", editable=True, delegate=BooleanDelegate())
