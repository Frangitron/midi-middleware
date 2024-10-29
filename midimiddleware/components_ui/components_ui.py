from dataclasses import dataclass

from pythonhelpers.singleton_metaclass import SingletonMetaclass


@dataclass
class ComponentsUi(metaclass=SingletonMetaclass):
    actions = None
    main_window = None
    port_selector = None
    monitor = None
    table = None
