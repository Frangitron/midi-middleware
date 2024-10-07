from PySide6.QtWidgets import QGridLayout, QWidget

from midimiddleware.ui_components.table import Table
from midimiddleware.ui_components.ui_components import UiComponents


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.table = Table()

        layout = QGridLayout()

        layout.addWidget(self.table, 0, 0)
        layout.addWidget(UiComponents().monitor, 1, 0)
        layout.addWidget(UiComponents().port_selector, 0, 1, 2, 1)

        self.setLayout(layout)
