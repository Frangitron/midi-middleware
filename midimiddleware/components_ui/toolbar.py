import os.path
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QPixmap
import sys

from midimiddleware.components_ui.components_ui import ComponentsUi
from pyside6helpers import icons, css
from pyside6helpers.css.editor import CSSEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        print(self.parent())

        # Set up the main window
        self.setWindowTitle("QToolbar with Checkable QAction Example")
        self.setGeometry(100, 100, 800, 600)

        # Create a checkable QAction
        self.checkable_action = QAction("Checkable Action")
        self.checkable_action.setIcon(icons.levels())
        self.checkable_action.setIconVisibleInMenu(True)
        self.checkable_action.setCheckable(True)

        self.button_action = QAction("Button Action")
        self.button_action.setIcon(icons.wifi())
        self.button_action.setIconVisibleInMenu(True)

        # Create a QToolBar
        self.toolbar = QToolBar("My Toolbar", self)
        self.toolbar.setOrientation(Qt.Horizontal)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolbar.orientationChanged.connect(self._update_button_style)
        self.addToolBar(self.toolbar)

        # Add the QAction to the toolbar
        self.toolbar.addWidget(QLabel('Test'))
        self.toolbar.addAction(self.checkable_action)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(QLabel('Testouille'))
        self.toolbar.addAction(self.button_action)

        # menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(self.checkable_action)
        file_menu.addSeparator()
        file_menu.addAction(self.button_action)

        # FRANGITRON
        logo_filepath = os.path.join("../resources/frangitron-logo.png")
        logo_pixmap = QPixmap(logo_filepath)
        logo_label = QLabel()
        logo_label.setPixmap(logo_pixmap)
        self.statusBar().addPermanentWidget(logo_label)


    def _update_button_style(self):
        if self.toolbar.orientation() == Qt.Vertical:
            self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        elif self.toolbar.orientation() == Qt.Horizontal:
            self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # css.load_onto(window)
    editor = CSSEditor("Frangitron")

    sys.exit(app.exec())
