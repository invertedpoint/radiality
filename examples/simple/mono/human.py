"""
radiality:examples:simple:mono:human
"""

from radiality import event
from radiality import Eventer
from radiality import effect
from radiality import Effector


class Human(Eventer):

    @event
    async def hello_said(self):
        """
        self: human.HumanCore
        """
        print('Hello! -- {0} said.'.format(self._name))


class Family(Effector):

    @effect
    async def gathered(self):
        """
        self: human.HumanCore
        """
        # Causes the `hello_said` event
        await self.hello_said()


class Animal(Effector):

    @effect
    async def sound_made(self, name):
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
