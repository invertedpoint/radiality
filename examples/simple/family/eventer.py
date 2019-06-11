"""
radiality:examples:simple:family:eventer
"""

from radiality import event
from radiality import Eventer


class Family(Eventer):
    """
    TODO: Add docstring
    """

    @event
    async def gathering(self) -> None:
        """
        TODO: Add docstring
        """
        pass

    @event
    async def gathered(self) -> None:
        """
        TODO: Add docstring
        """
        pass
