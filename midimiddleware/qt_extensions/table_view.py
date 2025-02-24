from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QTableView


class TableView(QTableView):
    """
    QTableView with deletion key functionality
    """

    rowDeletionRequested = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Delete, Qt.Key_Backspace):
            rows = [index.row() for index in self.selectionModel().selectedIndexes()]
            rows = list(set(rows))

            for row in rows:
                self.rowDeletionRequested.emit(row)

        super().keyPressEvent(event)
