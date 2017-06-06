"""
radiality:radiality.linear.ring.eventer

The `radiality/linear/ring/eventer.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from radiality.linear.event import sync_event
from radiality.linear.eventer import SyncEventer


class SyncRing(SyncEventer):

    @sync_event
    def subsystemized(self, cores):
        """
        self: radiality.linear.ring.core.SyncRing
        cores: defaultdict[str, List[SyncEventer]]
        """
        pass
