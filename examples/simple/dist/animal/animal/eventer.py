"""
radiality:examples:simple:dist:animal:animal.eventer
"""

from radiality import event
from radiality import Eventer


class Animal(Eventer):

    @event
    async def sound_made(self, name):
        """
        self: animal.core.Animal
        name: str
        """
        pass
