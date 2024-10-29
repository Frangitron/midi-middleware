import sys

from PySide6.QtWidgets import QApplication

from pyside6helpers import css
from pyside6helpers import resources as ps6_resources

from midimiddleware.components import resources
from midimiddleware.components.components import Components
from midimiddleware.components.message_translator import MessageTranslator
from midimiddleware.components.midi.devices import Devices
from midimiddleware.components.project_persistence import ProjectPersistence

from midimiddleware.components_ui.actions import Actions
from midimiddleware.components_ui.components_ui import ComponentsUi
from midimiddleware.components_ui.main_window_factory import create_main_window
from midimiddleware.components_ui.monitor import Monitor
from midimiddleware.components_ui.port_selector import PortSelector
from midimiddleware.components_ui.table import Table
from midimiddleware.components_ui.table_model import TableModel


class Launcher:

    def __init__(self):
        Components().configuration.resources_folder = resources.make_path()
        Components().devices = Devices()
        Components().project_persistence = ProjectPersistence()
        Components().translator = MessageTranslator()
        ps6_resources.set_root(resources.make_path())  # PyInstaller does not bundle dependencies resources ?

    def exec(self):
        app = QApplication()

        ComponentsUi().actions = Actions()
        ComponentsUi().monitor = Monitor()
        ComponentsUi().port_selector = PortSelector()
        ComponentsUi().table = Table()
        ComponentsUi().table.set_model(TableModel())

        app.aboutToQuit.connect(Components().devices.close_ports)

        css.load_onto(app)
        ComponentsUi().actions.create_actions(app)

        main_window = create_main_window(app)
        main_window.show()

        sys.exit(app.exec())
