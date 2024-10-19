import mido

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

from midimiddleware.components.components import Components
from midimiddleware.components_ui.components_ui import ComponentsUi
from pyside6helpers import icons, group

from midimiddleware.components_ui.monitor_line import MonitorLine
from midimiddleware.python_extensions.call_rate_limiter import rate_limit


class Monitor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._message: mido.Message | None = None

        self.line_device_in = MonitorLine("Device in")
        self.line_device_out = MonitorLine("Device out")
        self.line_virtual_out = MonitorLine("Virtual out")

        self.button_add_to_table = QPushButton("Add to table")
        self.button_add_to_table.setIcon(icons.plus())
        self.button_add_to_table.clicked.connect(self._add_to_table_clicked)

        group_ = group.make_group(
            title="Monitor", orientation=Qt.Vertical, widgets=[
                self.line_device_in, self.line_device_out, self.line_virtual_out,
                self.button_add_to_table
            ]
        )

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(group_)

    @rate_limit()
    def set_messages(self, device_in: mido.Message, device_out: mido.Message, virtual_out: mido.Message):
        self._message = device_in

        self.line_device_in.set_message(device_in)
        self.line_device_out.set_message(device_out)
        self.line_virtual_out.set_message(virtual_out)

    def clear(self):
        self.line_device_in.clear()
        self.line_device_out.clear()
        self.line_virtual_out.clear()

    def _add_to_table_clicked(self):
        Components().translator.add_message(self._message)
        ComponentsUi().table.refresh()
