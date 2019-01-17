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
    async def gathered(self) -> None:
        """
        TODO: Add docstring
        """
        pass
