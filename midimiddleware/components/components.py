from dataclasses import dataclass

from midimiddleware.components.configuration import Configuration
from midimiddleware.components.engine import Engine
from midimiddleware.components.port_selector import PortSelector
from midimiddleware.components.project_persitence import ProjectPersistence
from midimiddleware.python_extensions.singleton_metaclass import SingletonMetaclass


@dataclass
class Components(metaclass=SingletonMetaclass):
    configuration = Configuration()
    engine = Engine()
    port_selector = PortSelector()
    project_persistence = ProjectPersistence()
