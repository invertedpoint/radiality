"""
radiality:examples:poly:animal.core
"""

from animal import eventer
from animal import effectors


class Animal(eventer.Animal, effectors.Human):
    _name = None  # type: str

    def __init__(self, name):
        """
        self: animal.core.Animal
        name: str
        """
        super().__init__()

        self._name = name


class Dog(Animal):
    pass
