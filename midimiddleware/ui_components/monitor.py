import mido
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton

from pyside6helpers import icons, group


class _MonitorLine(QWidget):
    def __init__(self, caption, parent=None):
        super().__init__(parent)

        self.label_caption = QLabel(caption)

        self.label_caption.setStyleSheet("font: bold")
        self.label_caption.setFixedWidth(80)

        self.label_channel = QLabel("Channel: --")
        self.label_channel.setFixedWidth(70)

        self.label_type = QLabel("Type: --")
        self.label_type.setFixedWidth(130)

        self.label_id = QLabel("ID: --")
        self.label_id.setFixedWidth(50)

        self.label_value = QLabel("Value: --")
        self.label_value.setFixedWidth(80)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label_caption)
        layout.addWidget(self.label_channel)
        layout.addWidget(self.label_type)
        layout.addWidget(self.label_id)
        layout.addWidget(self.label_value)
        layout.addStretch()

    def clear(self):
        self.label_channel = QLabel("Channel: --")
        self.label_type = QLabel("Type: --")
        self.label_id = QLabel("ID: --")
        self.label_value = QLabel("Value: --")

    def set_message(self, message: mido.Message | None):
        if message is None:
            self.clear()
            return

        self.label_channel.setText(f"Channel: {message.channel + 1}")
        self.label_type.setText(f"Type: {message.type}")

        if message.type == 'note_on':
            self.label_id.setText(f"ID: {message.note}")
            self.label_value.setText(f"Velocity: {message.velocity}")

        elif message.type == 'pitchwheel':
            self.label_id.setText(f"ID: --")
            self.label_value.setText(f"Pitch: {message.pitch}")

        elif message.type == 'control_change':
            self.label_id.setText(f"ID: {message.control}")
            self.label_value.setText(f"Value: {message.value}")


class Monitor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.line_device_in = _MonitorLine("Device in")
        self.line_device_out = _MonitorLine("Device out")
        self.line_virtual_out = _MonitorLine("Virtual out")

        self.button_add_to_table = QPushButton("Add to table")
        self.button_add_to_table.setIcon(icons.plus())
        self.button_add_to_table.setEnabled(False)

        group_ = group.make_group(
            title="Monitor", orientation=Qt.Vertical, widgets=[
                self.line_device_in, self.line_device_out, self.line_virtual_out,
                self.button_add_to_table
            ]
        )

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(group_)

    def set_messages(self, device_in: mido.Message, device_out: mido.Message, virtual_out: mido.Message):
        self.line_device_in.set_message(device_in)
        self.line_device_out.set_message(device_out)
        self.line_virtual_out.set_message(virtual_out)
