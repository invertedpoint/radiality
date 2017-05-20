"""
radiality:radiality.linear.ring

The `radiality/linear/ring.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from collections import defaultdict

from radiality.linear.eventer import sync_event
from radiality.linear.eventer import SyncEventer


class Ring(SyncEventer):

    @sync_event
    def systemized(self, cores):
        """
        self: SyncRing
        cores: defaultdict[str, List[SyncEventer]]
        """
        pass


class SyncRing(Ring):
    """
    Dispatcher of cores
    """
    _cores = None  # type: defaultdict[str, List[SyncEventer]]

    def __init__(self):
        """
        self: SyncRing
        """
        super().__init__()

        self._cores = defaultdict(list)

    def focus(self, core):
        """
        self: SyncRing
        core: SyncEventer

        return: SyncEventer

        Overridden from `SyncEventer`.
        """
        super().focus(core)
        # Registers the core
        self._cores[core.CORE_ID].append(core)
        # Causes the `systemized` event
        self.systemized(cores=self._cores)

        return core
