from PySide6.QtWidgets import QApplication

from midimiddleware.ui_components.main_window.widget import MainWindow
from midimiddleware.ui_components.central_widget import CentralWidget

from midimiddleware.ui_components.ui_components import UiComponents


def create_main_window(app: QApplication) -> MainWindow:
    main_window = MainWindow()
    main_window.setCentralWidget(CentralWidget())

    menu_bar = main_window.menuBar()
    file_menu = menu_bar.addMenu("&File")
    file_menu.addAction(UiComponents().actions.new)
    file_menu.addAction(UiComponents().actions.open)
    file_menu.addAction(UiComponents().actions.save)
    file_menu.addSeparator()
    file_menu.addAction(UiComponents().actions.quit)

    UiComponents().actions.new.setEnabled(False)

    return main_window
