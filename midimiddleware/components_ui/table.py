from dataclasses import fields

from PySide6.QtWidgets import QGroupBox, QTableView, QHBoxLayout

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
