from PySide6.QtCore import QObject
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMenu

from pyside6helpers import icons


class Actions(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.new: QAction = None
        self.load: QAction = None
        self.save: QAction = None
        self.quit: QAction = None

    def create_actions(self, app: QApplication):
        self.new = QAction(icons.file(), "&New project")

        self.load = QAction(icons.folder(), "&Load project...")

        self.save = QAction(icons.diskette(), "&Save project...")

        self.quit = QAction(icons.right_arrow(), "&Quit")
        self.quit.triggered.connect(app.quit)
