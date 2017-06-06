"""
radiality:examples:simple:sync_mono:animal
"""

from radiality.linear import event
from radiality.linear import Eventer
from radiality.linear import effect
from radiality.linear import Effector


class Animal(Eventer):

    @event
    def sound_made(self, name):
        """
        self: animal.AnimalCore
        name: str
        """
        pass


class Human(Effector):

    @effect
    def hello_said(self):
        """
        self: animal.AnimalCore
        """
        # Causes the `sound_made` event
        self.sound_made(name=self._name)


class AnimalCore(Animal, Human):
    _name = None  # type: str

    def __init__(self, name):
        """
        self: animal.AnimalCore
        name: str
        """
        super().__init__()

        self._name = name


class DogCore(AnimalCore):
    pass
