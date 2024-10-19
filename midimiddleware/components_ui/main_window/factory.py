from PySide6.QtWidgets import QApplication

from midimiddleware.apis import project_persistence
from midimiddleware.components_ui.central_widget import CentralWidget
from midimiddleware.components_ui.main_window.widget import MainWindow
from midimiddleware.components_ui.components_ui import ComponentsUi


def create_main_window(app: QApplication) -> MainWindow:
    main_window = MainWindow()
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
