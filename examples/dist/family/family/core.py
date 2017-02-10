"""
radiality:examples:poly:family.core
"""

from family import eventer
from human.core import Man
from human.core import Woman
from animal.core import Dog


class Family(eventer.Family):
    _tom = None  # type: Man
    _mary = None  # type: Woman
    _buddy = None  # type: Dog

    def attract(self, ring):
        """
        self: family.core.Family
        ring: radiality.Ring
        """
        ring.focus(self)

        self._tom = ring.focus(Man(name='Tom'))
        self._mary = ring.focus(Woman(name='Mary'))
        self._buddy = ring.focus(Dog(name='Buddy'))

        return self

    def gather(self):
        """
        self: family.core.Family
        """
        # Causes the `gathered` event
        self.gathered()
