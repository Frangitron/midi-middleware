import os.path

from PySide6.QtWidgets import QApplication

from pyside6helpers import icons
from pyside6helpers.main_window import MainWindow

from midimiddleware.apis import project_persistence
from midimiddleware.components.components import Components
from midimiddleware.components_ui.central_widget import CentralWidget
from midimiddleware.components_ui.components_ui import ComponentsUi


def create_main_window(app: QApplication) -> MainWindow:
    main_window = MainWindow(
        logo_filepath=os.path.join(Components().configuration.resources_folder, "frangitron-logo.png"),
        settings_tuple=("Frangitron", "MIDI Middleware")
    )
    main_window.setWindowTitle("MIDI Middleware")
    main_window.setWindowIcon(icons.levels())
    main_window.setCentralWidget(CentralWidget())
    main_window.shown.connect(project_persistence.open_last_saved)

    menu_bar = main_window.menuBar()
    file_menu = menu_bar.addMenu("&File")
    file_menu.addAction(ComponentsUi().actions.new)
    file_menu.addAction(ComponentsUi().actions.open)
    file_menu.addAction(ComponentsUi().actions.save)
    file_menu.addSeparator()
    file_menu.addAction(ComponentsUi().actions.quit)

    ComponentsUi().main_window = main_window

    return main_window
