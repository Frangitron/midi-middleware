from dataclasses import fields, Field

from PySide6.QtCore import QAbstractTableModel, Qt

from midimiddleware.components.components import Components
from midimiddleware.components.message_translation_info import MessageTranslationInfo
from midimiddleware.components_ui.table_message_translation_info import AttributeUiInfo, TableMessageTranslationInfo


class TableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._fields: list[Field[AttributeUiInfo]] = fields(TableMessageTranslationInfo)

    def rowCount(self, parent=None):
        return Components().translator.count()

    def columnCount(self, parent=None):
        return len(self._fields)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        elif role != Qt.DisplayRole:
            return None

        translation: MessageTranslationInfo = Components().translator.get(index.row())
        return str(getattr(translation, self._fields[index.column()].name))

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self._fields[section].default.caption

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled

        if self._fields[index.column()].default.editable:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

        return Qt.ItemIsSelectable | Qt.ItemIsEnabled