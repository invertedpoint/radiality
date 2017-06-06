"""
radiality:examples:simple:mono:animal
"""

from radiality import event
from radiality import Eventer
from radiality import effect
from radiality import Effector


class Animal(Eventer):

    @event
    async def sound_made(self, name):
        """
        self: animal.AnimalCore
        name: str
        """
        pass


class Human(Effector):

    @effect
    async def hello_said(self):
        """
        self: animal.AnimalCore
        """
        # Causes the `sound_made` event
        await self.sound_made(name=self._name)


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
