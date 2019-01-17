"""
radiality:examples:simple:animal:eventer
"""

from radiality import event
from radiality import Eventer


class Animal(Eventer):
    """
    TODO: Add docstring
    """

    @event
    async def sound_made(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        pass
