"""
radiality:examples:mono:family
"""

from radiality import event
from radiality import Eventer

from human import ManCore
from human import WomanCore
from animal import DogCore


class Family(Eventer):

    @event
    def gathered(self):
        pass


class FamilyCore(Family):
    _tom = None  # type: ManCore
    _mary = None  # type: WomanCore
    _buddy = None  # type: DogCore

    def attract(self, ring):
        ring.focus(self)

        self._tom = ring.focus(ManCore(name='Tom'))
        self._mary = ring.focus(WomanCore(name='Mary'))
        self._buddy = ring.focus(DogCore(name='Buddy'))

        return self

    def gather(self):
        # Causes the `gathered` event
        self.gathered()
