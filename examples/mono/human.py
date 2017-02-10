"""
radiality:examples:mono:human
"""

from radiality import event
from radiality import Eventer
from radiality import effect
from radiality import Effector


class Human(Eventer):

    @event
    def hello_said(self):
        print('Hello! -- {0} said.'.format(self._name))


class Family(Effector):

    @effect
    def gathered(self):
        # Causes the `hello_said` event
        self.hello_said()


class Animal(Effector):

    @effect
    def sound_made(self, name):
        print('{0} made a sound! -- {1} said.'.format(name, self._name))


class HumanCore(Human, Family, Animal):
    _name = None  # type: str

    def __init__(self, name):
        super().__init__()

        self._name = name


class ManCore(HumanCore):
    pass


class WomanCore(HumanCore):
    pass
