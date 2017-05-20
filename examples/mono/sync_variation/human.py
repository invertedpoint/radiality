"""
radiality:examples:mono:sync_variation:human
"""

from radiality.linear import event
from radiality.linear import Eventer
from radiality.linear import effect
from radiality.linear import Effector


class Human(Eventer):

    @event
    def hello_said(self):
        """
        self: human.HumanCore
        """
        print('Hello! -- {0} said.'.format(self._name))


class Family(Effector):

    @effect
    def gathered(self):
        """
        self: human.HumanCore
        """
        # Causes the `hello_said` event
        self.hello_said()


class Animal(Effector):

    @effect
    def sound_made(self, name):
        """
        self: human.HumanCore
        name: str
        """
        print('{0} made a sound! -- {1} said.'.format(name, self._name))


class HumanCore(Human, Family, Animal):
    _name = None  # type: str

    def __init__(self, name):
        """
        self: human.HumanCore
        name: str
        """
        super().__init__()

        self._name = name


class ManCore(HumanCore):
    pass


class WomanCore(HumanCore):
    pass
