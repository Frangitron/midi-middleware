import os.path

from PySide6.QtCore import QObject
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication

from pyside6helpers import icons, load_save_dialog

from midimiddleware.ui_components.ui_components import UiComponents
from midimiddleware.apis import project_persistence


class Actions(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.new: QAction = None
        self.open: QAction = None
        self.save: QAction = None
        self.quit: QAction = None

    def create_actions(self, app: QApplication):
        self.new = QAction(icons.file(), "&New project")

        self.open = QAction(icons.folder(), "&Open project...")
        self.open.triggered.connect(load_save_dialog.make_open_hook(
            title="Open project", name_filter="JSON (*.json)", working_directory=os.path.expanduser("~"),
            callback=project_persistence.open, parent=UiComponents().main_window
        ))

        self.save = QAction(icons.diskette(), "&Save project...")
        self.save.triggered.connect(load_save_dialog.make_save_hook(
            title="Save project", name_filter="JSON (*.json)", working_directory=os.path.expanduser("~"),
            callback=project_persistence.save, parent=UiComponents().main_window
        ))

        self.quit = QAction(icons.right_arrow(), "&Quit")
        self.quit.triggered.connect(app.quit)
