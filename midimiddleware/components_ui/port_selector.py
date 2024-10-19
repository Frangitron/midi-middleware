from PySide6.QtWidgets import QComboBox, QLabel, QGridLayout, QPushButton, QWidget

from pyside6helpers import combo, group, icons, error_reporting, hourglass

from midimiddleware.components.components import Components


class PortSelector(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._in_ports: list[str] = list()
        self._out_ports: list[str] = list()

        self.device_in_port_combo_box = QComboBox()
        self.device_in_port_combo_box.currentIndexChanged.connect(self.update_button_color)
        self.device_out_port_combo_box = QComboBox()
        self.device_out_port_combo_box.currentIndexChanged.connect(self.update_button_color)
        self.virtual_out_port_combo_box = QComboBox()
        self.virtual_out_port_combo_box.currentIndexChanged.connect(self.update_button_color)

        self.reload_ports_button = QPushButton("Reload")
        self.reload_ports_button.setToolTip("Reload list of available MIDI ports")
        self.reload_ports_button.setMinimumWidth(100)
        self.reload_ports_button.setIcon(icons.refresh())
        self.reload_ports_button.clicked.connect(self.reload_ports)

        self.apply_button = QPushButton("Apply")
        self.apply_button.setToolTip("Open selected ports for listening and sending")
        self.apply_button.setMinimumWidth(100)
        self.apply_button.setIcon(icons.check())
        self.apply_button.clicked.connect(self.apply)

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(group.make_group_grid(
            title="MIDI Controller ports",
            widgets=(
                (QLabel("In"), self.device_in_port_combo_box),
                (QLabel("Out"), self.device_out_port_combo_box)
            ),
            stretch_last_column=True
        ), 0, 0, 1, 2)
        layout.addWidget(group.make_group_grid(
            title="MIDI Virtual ports",
            widgets=(
                (QLabel("Out"), self.virtual_out_port_combo_box),
            ),
            stretch_last_column=True
        ), 1, 0, 1, 2)

        layout.addWidget(self.reload_ports_button, 2, 0)
        layout.addWidget(self.apply_button, 2, 1)

        layout.addWidget(QWidget())
        layout.setRowStretch(layout.count() - 1, 1)
        self.setLayout(layout)

    @error_reporting.error_reported("Reload available ports")
    def reload_ports(self):
        self._in_ports = Components().port_selector.get_input_ports()
        self._out_ports = Components().port_selector.get_output_ports()

        combo.update(
            self.device_in_port_combo_box,
            self._in_ports,
            Components().port_selector.device_in_name,
            reset=True
        )
        combo.update(
            self.device_out_port_combo_box,
            self._out_ports,
            Components().port_selector.device_out_name,
            reset=True
        )
        combo.update(
            self.virtual_out_port_combo_box,
            self._out_ports,
            Components().port_selector.virtual_out_name,
            reset=True
        )

    @error_reporting.error_reported("Apply port selection")
    def apply(self):
        # FIXME: this method should be more readable
        device_in_index = self.device_in_port_combo_box.currentIndex()
        device_out_index = self.device_out_port_combo_box.currentIndex()
        virtual_out_index = self.virtual_out_port_combo_box.currentIndex()

        selected_out_ports = [
            self._out_ports[device_out_index] if device_out_index >= 0 else "",
            self._out_ports[virtual_out_index] if virtual_out_index >= 0 else ""
        ]

        check_doubles = list()
        for port in selected_out_ports:
            if port and port in check_doubles:
                raise ValueError(f"An out port can only be selected once: {port}")
            else:
                check_doubles.append(port)

        # FIXME: this block should be in an API
        with hourglass.Hourglass():
            Components().engine.stop()
            Components().port_selector.select_ports(
                device_in=self._in_ports[device_in_index] if device_out_index >= 0 else "",
                device_out=selected_out_ports[0],
                virtual_out=selected_out_ports[1]
            )
            Components().engine.start()

        self.update_button_color()

    def update_button_color(self):
        combos = [
            self.device_in_port_combo_box,
            self.device_out_port_combo_box,
            self.virtual_out_port_combo_box
        ]
        names = [
            Components().port_selector.device_in_name,
            Components().port_selector.device_out_name,
            Components().port_selector.virtual_out_name
        ]
        red_needed = [combo.currentText() not in name for combo, name in zip(combos, names)]
        if any(red_needed):
            self.apply_button.setStyleSheet("background-color: rgb(128, 30, 30)")
        else:
            self.apply_button.setStyleSheet("")
