from PySide6.QtCore import QSettings

from midimiddleware.components.components import Components
from midimiddleware.components_ui.components_ui import ComponentsUi


def new():
    Components().project_persistence.reset()
    ComponentsUi().port_selector.reload_ports()
    ComponentsUi().monitor.clear()
    ComponentsUi().table.refresh()


def open_last_saved():
    settings = QSettings("Frangitron", "MIDI Middleware")
    filepath = settings.value('last_saved_project')
    open_(filepath)


def open_(filepath):
    Components().project_persistence.open(filepath)
    ComponentsUi().port_selector.reload_ports()
    ComponentsUi().monitor.clear()
    ComponentsUi().table.refresh()


def save(filepath):
    Components().project_persistence.save(filepath)
    settings = QSettings("Frangitron", "MIDI Middleware")
    settings.setValue('last_saved_project', filepath)
