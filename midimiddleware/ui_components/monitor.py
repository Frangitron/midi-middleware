import mido
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QPushButton

from pyside6helpers import icons, group


class Monitor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label_channel = QLabel()
        self.label_type = QLabel()
        self.label_id = QLabel()
        self.label_value = QLabel()

        self.button_add_to_table = QPushButton("Add to table")
        self.button_add_to_table.setIcon(icons.plus())

        group_ = group.make_group(
            title="Monitor", orientation=Qt.Horizontal, widgets=[
                self.label_channel,
                self.label_type,
                self.label_id,
                self.label_value,
                self.button_add_to_table
            ]
        )

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(group_)
        self.setLayout(layout)

        self._message = None

    def set_message(self, message: mido.Message):
        self._message = message

        self.label_channel.setText(f"Channel: {message.channel + 1}")
        self.label_type.setText(f"Type: {message.type}")

        if message.type == 'note_on':
            self.label_id.setText(f"ID: {message.note}")
            self.label_value.setText(f"Valocity: {message.velocity}")
        elif message.type == 'pitchwheel':
            self.label_id.setText(f"ID: --")
            self.label_value.setText(f"Pitch: {message.pitch}")
        elif message.type == 'control_change':
            self.label_id.setText(f"ID: {message.control}")
            self.label_value.setText(f"Value: {message.value}")
