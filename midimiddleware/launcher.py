import sys

from PySide6.QtWidgets import QApplication

from pyside6helpers import css
from pyside6helpers import resources as ps6_resources

from midimiddleware.components import resources
from midimiddleware.components.components import Components
from midimiddleware.components.project_persitence import ProjectPersistence
from midimiddleware.ui_components.actions import Actions
from midimiddleware.ui_components.main_window.factory import create_main_window
from midimiddleware.ui_components.port_selector import PortSelector
from midimiddleware.ui_components.ui_components import UiComponents


class Launcher:

    def __init__(self):
        Components().configuration.resources_folder = resources.make_path()
        Components().project_persistence = ProjectPersistence()
        ps6_resources.set_root(resources.make_path())  # PyInstaller does not bundle dependencies resources ?

    def exec(self):
        app = QApplication()

        UiComponents().actions = Actions()
        UiComponents().port_selector = PortSelector()

        app.aboutToQuit.connect(Components().engine.stop)
        app.aboutToQuit.connect(Components().port_selector.close)

        css.load_onto(app)
        UiComponents().actions.create_actions(app)

        main_window = create_main_window(app)
        main_window.show()

        sys.exit(app.exec())
