"""
radiality:examples:poly:family.eventer
"""

from radiality import event
from radiality import Eventer


class Family(Eventer):

    @event
    def gathered(self):
        """
        self: family.core.Family
        """
        pass
