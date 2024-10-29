from dataclasses import dataclass

from pythonhelpers.singleton_metaclass import SingletonMetaclass

from midimiddleware.components.configuration import Configuration
from midimiddleware.components.midi.port_selector import PortSelector


@dataclass
class Components(metaclass=SingletonMetaclass):
    configuration = Configuration()
    devices = None
    port_selector = PortSelector()
    project_persistence = None
    translator = None
