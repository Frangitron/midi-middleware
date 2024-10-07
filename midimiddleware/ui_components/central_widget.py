from PySide6.QtWidgets import QHBoxLayout, QWidget

from midimiddleware.ui_components.port_selector import PortSelector
from midimiddleware.ui_components.table import Table


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.table = Table()
        self.port_selector = PortSelector()

        layout = QHBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.port_selector)
        self.setLayout(layout)
