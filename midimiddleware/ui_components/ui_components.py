from dataclasses import dataclass

from midimiddleware.python_extensions.singleton_metaclass import SingletonMetaclass


@dataclass
class UiComponents(metaclass=SingletonMetaclass):
    actions = None
    main_window = None
    port_selector = None
    monitor = None
