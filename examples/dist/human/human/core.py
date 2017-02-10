"""
radiality:examples:poly:human.core
"""

from human import eventer
from human import effectors


class Human(eventer.Human, effectors.Family, effectors.Animal):
    _name = None  # type: str

    def __init__(self, name):
        """
        self: human.core.Human
        name: str
        """
        super().__init__()

        self._name = name


class Man(Human):
    pass


class Woman(Human):
    pass
