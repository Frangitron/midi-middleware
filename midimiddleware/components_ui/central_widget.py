from PySide6.QtWidgets import QGridLayout, QWidget

from midimiddleware.components_ui.components_ui import ComponentsUi


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QGridLayout(self)

        layout.addWidget(ComponentsUi().table, 0, 0)
        layout.addWidget(ComponentsUi().monitor, 1, 0)
        layout.addWidget(ComponentsUi().port_selector, 0, 1, 2, 1)
