from PySide6.QtWidgets import QTableView


class Table(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
