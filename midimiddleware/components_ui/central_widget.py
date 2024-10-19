from PySide6.QtWidgets import QGridLayout, QWidget

from midimiddleware.components_ui.table import Table
from midimiddleware.components_ui.components_ui import ComponentsUi


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.table = Table()

        layout = QGridLayout()

        layout.addWidget(self.table, 0, 0)
        layout.addWidget(ComponentsUi().monitor, 1, 0)
        layout.addWidget(ComponentsUi().port_selector, 0, 1, 2, 1)

        self.setLayout(layout)
