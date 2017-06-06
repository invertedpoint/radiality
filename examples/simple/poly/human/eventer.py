"""
radiality:examples:simple:poly:human.eventer
"""

from radiality import event
from radiality import Eventer


class Human(Eventer):

    @event
    async def hello_said(self):
        """
        self: human.core.Human
        """
        print('Hello! -- {0} said.'.format(self._name))
