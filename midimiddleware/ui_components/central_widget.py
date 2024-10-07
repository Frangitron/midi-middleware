from PySide6.QtWidgets import QComboBox, QLabel, QHBoxLayout, QPushButton, QWidget

from pyside6helpers import group
from pyside6helpers import icons

from midimiddleware.ui_components.ports_selector import PortsSelector
from midimiddleware.ui_components.table import Table

class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.table = Table()
        self.port_selector = PortsSelector()

        layout = QHBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.port_selector)
        self.setLayout(layout)
