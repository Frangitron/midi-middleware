import sys

from PySide6.QtWidgets import QApplication
from pyside6helpers import css
from pyside6helpers import resources as ps6_resources

from midimiddleware.components import resources
from midimiddleware.components.ui.main_window import MainWindow
from midimiddleware.core.components import Components


class Launcher:

    def __init__(self):
        Components().configuration.resources_folder = resources.make_path()
        ps6_resources.set_root(resources.make_path())  # PyInstaller does not bundle modules resources ?

    def exec(self):
        app = QApplication()
        css.load_onto(app)

        main_window = MainWindow()
        main_window.show()

        sys.exit(app.exec())
