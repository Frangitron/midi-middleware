import mido
from dataclasses import fields

from PySide6.QtWidgets import QGroupBox, QTableView, QHBoxLayout

from pythonhelpers.call_rate_limiter import rate_limit

from midimiddleware.components.components import Components
from midimiddleware.components_ui.table_message_translation_info import TableMessageTranslationInfo


class Table(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Table")

        self._table_view = QTableView()
        self._table_view.setShowGrid(False)
        self._table_view.setAlternatingRowColors(True)

        for index, field in enumerate(fields(TableMessageTranslationInfo)):
            if field.default.delegate is None:
                continue
            delegate = field.default.delegate
            self._table_view.setItemDelegateForColumn(index, delegate)

        layout = QHBoxLayout(self)
        layout.addWidget(self._table_view)

    def set_model(self, model):
        self._table_view.setModel(model)

    def refresh(self):
        self._table_view.model().beginResetModel()
        self._table_view.model().endResetModel()

    @rate_limit()
    def select_translation_from_message(self, message: mido.Message):
        index = Components().translator.translation_index_from_message(message)
        if index != -1:
            self._table_view.selectRow(index)
        else:
            self._table_view.clearSelection()
