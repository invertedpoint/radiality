"""
radiality:examples:poly:human.effectors
"""

from radiality import effect
from radiality import Effector


class Family(Effector):

    @effect
    def gathered(self):
        """
        self: human.core.Human
        """
        # Causes the `hello_said` event
        self.hello_said()


class Animal(Effector):

    @effect
    def sound_made(self, name):
        """
        self: human.core.Human
        name: str
        """
        print('{0} made a sound! -- {1} said.'.format(name, self._name))
