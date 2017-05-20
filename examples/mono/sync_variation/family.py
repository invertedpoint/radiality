"""
radiality:examples:mono:sync_variation:family
"""

from radiality.linear import event
from radiality.linear import Eventer

from human import ManCore
from human import WomanCore
from animal import DogCore


class Family(Eventer):

    @event
    def gathered(self):
        """
        self: family.FamilyCore
        """
        pass


class FamilyCore(Family):
    _tom = None  # type: ManCore
    _mary = None  # type: WomanCore
    _buddy = None  # type: DogCore

    def attract(self, ring):
        """
        self: family.FamilyCore
        ring: radiality.Ring
        """
        ring.focus(self)

        self._tom = ring.focus(ManCore(name='Tom'))
        self._mary = ring.focus(WomanCore(name='Mary'))
        self._buddy = ring.focus(DogCore(name='Buddy'))

        return self

    def gather(self):
        """
        self: family.FamilyCore
        """
        # Causes the `gathered` event
        self.gathered()
