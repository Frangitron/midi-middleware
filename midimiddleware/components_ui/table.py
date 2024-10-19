from PySide6.QtWidgets import QGroupBox, QTableView, QHBoxLayout


class Table(QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Table")

        layout = QHBoxLayout(self)
        layout.addWidget(QTableView())

    def message_added(self):
        # TODO: QAbstractTableModel etc
        raise NotImplementedError
