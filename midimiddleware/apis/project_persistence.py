from PySide6.QtCore import QSettings

from midimiddleware.components.components import Components
from midimiddleware.ui_components.ui_components import UiComponents


def open_last_saved():
    settings = QSettings("Frangitron", "MIDI Middleware")
    filepath = settings.value('last_saved_project')
    Components().project_persistence.open(filepath)
    UiComponents().port_selector.reload_ports()


def open(filepath):
    Components().project_persistence.open(filepath)
    UiComponents().port_selector.reload_ports()


def save(filepath):
    Components().project_persistence.save(filepath)
    settings = QSettings("Frangitron", "MIDI Middleware")
    settings.setValue('last_saved_project', filepath)
