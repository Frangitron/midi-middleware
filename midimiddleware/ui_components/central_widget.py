from PySide6.QtWidgets import QHBoxLayout, QWidget

from midimiddleware.ui_components.table import Table
from midimiddleware.ui_components.ui_components import UiComponents


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.table = Table()

        layout = QHBoxLayout()

        layout.addWidget(self.table)
        layout.addWidget(UiComponents().port_selector)

        self.setLayout(layout)
