"""
radiality:radiality.linear.ring.core

The `radiality/linear/ring/core.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from collections import defaultdict

from radiality.linear.ring import eventer


class SyncRing(eventer.SyncRing):
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
        # Causes the `subsystemized` event
        self.subsystemized(cores=self._cores)

        return core
