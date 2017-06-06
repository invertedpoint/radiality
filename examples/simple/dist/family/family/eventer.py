"""
radiality:examples:simple:dist:family.eventer
"""

from radiality import event
from radiality import Eventer


class Family(Eventer):

    @event
    async def gathered(self):
        """
        self: family.core.Family
        """
        pass
