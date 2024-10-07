from dataclasses import dataclass

from midimiddleware.core.configuration import Configuration
from midimiddleware.python_extensions.singleton_metaclass import SingletonMetaclass


@dataclass
class Components(metaclass=SingletonMetaclass):
    configuration = Configuration()
