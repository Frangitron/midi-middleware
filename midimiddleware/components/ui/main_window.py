import os.path

from PySide6.QtCore import QSettings
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QMainWindow

from pyside6helpers import icons

from midimiddleware.core.components import Components


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MIDI Middleware")
        self.setWindowIcon(icons.levels())

        logo_filepath = os.path.join(Components().configuration.resources_folder, "frangitron-logo.png")
        logo_pixmap = QPixmap(logo_filepath)
        logo_label = QLabel()
        logo_label.setPixmap(logo_pixmap)
        self.statusBar().addPermanentWidget(logo_label)

        self.load_geometry()

    def closeEvent(self, event):
        self.save_geometry()
        super().closeEvent(event)
        event.accept()

    def save_geometry(self):
        settings = QSettings("Frangitron", "MIDI Middleware")
        settings.setValue('geometry', self.saveGeometry())
        settings.setValue('state', self.saveState())

    def load_geometry(self):
        settings = QSettings("Frangitron", "MIDI Middleware")
        self.restoreGeometry(settings.value('geometry'))
        self.restoreState(settings.value('state'))
