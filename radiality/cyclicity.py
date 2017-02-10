"""
radiality:radiality.cyclicity

The `radiality/cyclicity.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from collections import defaultdict

from radiality.mutability import event
from radiality.mutability import Eventer


class Ringing(Eventer):

    @event
    def systemized(self, cores):
        """
        self: radiality.cyclicity.Ring
        cores: defaultdict[str, List[radiality.mutability.Eventer]]
        """
        pass


class Ring(Ringing):
    """
    Dispatcher of cores
    """
    _cores = None  # type: defaultdict[str, List[radiality.mutability.Eventer]]

    def __init__(self):
        """
        self: radiality.cyclicity.Ring
        """
        super().__init__()

        self._cores = defaultdict(list)

    def focus(self, core):
        """
        self: radiality.cyclicity.Ring
        core: radiality.mutability.Eventer

        Overridden from `radiality.mutability.Eventer`.
        """
        super().focus(core)
        # Registers the core
        self._cores[core.CORE_ID].append(core)
        # Causes the `systemized` event
        self.systemized(cores=self._cores)
