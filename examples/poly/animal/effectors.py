"""
radiality:examples:poly:animal.effectors
"""

from radiality import effect
from radiality import Effector


class Human(Effector):

    @effect
    def hello_said(self):
        """
        self: animal.core.Animal
        """
        # Causes the `sound_made` event
        self.sound_made(name=self._name)
