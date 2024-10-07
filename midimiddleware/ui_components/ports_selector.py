from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QPushButton, QWidget

from pyside6helpers import group
from pyside6helpers import icons


class PortsSelector(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.device_in_port_combo_box = QComboBox()
        self.device_out_port_combo_box = QComboBox()
        self.virtual_in_port_combo_box = QComboBox()
        self.virtual_out_port_combo_box = QComboBox()

        self.reload_ports_button = QPushButton("Reload available ports")
        self.reload_ports_button.setIcon(icons.refresh())

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(group.make_group_grid(
            title="MIDI Controller ports",
            widgets=(
                (QLabel("In"), self.device_in_port_combo_box),
                (QLabel("Out"), self.device_out_port_combo_box)
            ),
            stretch_last_column=True
        ))
        layout.addWidget(group.make_group_grid(
            title="MIDI Virtual ports",
            widgets=(
                (QLabel("In"), self.virtual_in_port_combo_box),
                (QLabel("Out"), self.virtual_out_port_combo_box)
            ),
            stretch_last_column=True
        ))
        layout.addWidget(self.reload_ports_button)
        layout.addWidget(QWidget())
        layout.setStretch(layout.count() - 1, 1)
        self.setLayout(layout)
