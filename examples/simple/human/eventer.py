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
    async def hello_said(self) -> None:
        """
        TODO: Add docstring
        """
        print(f'Hello! -- {self._name} said.')
