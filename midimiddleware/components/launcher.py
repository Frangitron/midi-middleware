import sys

from PySide6.QtWidgets import QApplication
from pyside6helpers import css
from pyside6helpers import resources as ps6_resources

from midimiddleware.components import resources
from midimiddleware.ui_components.main_window.factory import create_main_window
from midimiddleware.components.components import Components
from midimiddleware.ui_components.ui_components import UiComponents


class Launcher:

    def __init__(self):
        Components().configuration.resources_folder = resources.make_path()
        ps6_resources.set_root(resources.make_path())  # PyInstaller does not bundle modules resources ?

    def exec(self):
        app = QApplication()
        app.aboutToQuit.connect(Components().engine.stop)
        app.aboutToQuit.connect(Components().port_selector.close)

        css.load_onto(app)
        UiComponents().actions.create_actions(app)

        main_window = create_main_window(app)
        main_window.show()

        sys.exit(app.exec())
