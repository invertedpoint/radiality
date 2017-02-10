"""
radiality:examples:mono:animal
"""

from radiality import event
from radiality import Eventer
from radiality import effect
from radiality import Effector


class Animal(Eventer):

    @event
    def sound_made(self, name):
        pass


class Human(Effector):

    @effect
    def hello_said(self):
        # Causes the `sound_made` event
        self.sound_made(name=self._name)


class AnimalCore(Animal, Human):
    _name = None  # type: str

    def __init__(self, name):
        super().__init__()

        self._name = name


class DogCore(AnimalCore):
    pass
