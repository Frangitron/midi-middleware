from dataclasses import dataclass

from midimiddleware.ui_components.actions import Actions
from midimiddleware.python_extensions.singleton_metaclass import SingletonMetaclass


@dataclass
class UiComponents(metaclass=SingletonMetaclass):
    actions = Actions()
