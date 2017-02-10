"""
radiality:examples:poly:animal.eventer
"""

from radiality import event
from radiality import Eventer


class Animal(Eventer):

    @event
    def sound_made(self, name):
        """
        self: animal.core.Animal
        name: str
        """
        pass
