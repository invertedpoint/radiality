"""
radiality:examples:simple:human:eventer
"""

from radiality import event
from radiality import Eventer


class Human(Eventer):
    """
    TODO: Add docstring
    """

    @event
    async def came(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        pass

    @event
    async def hello_said(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        print(f'Hello! -- {name} said.')
