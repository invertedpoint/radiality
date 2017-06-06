"""
radiality:examples:simple:mono:family
"""

import asyncio

from radiality import event
from radiality import Eventer

from human import ManCore
from human import WomanCore
from animal import DogCore


class Family(Eventer):

    @event
    async def gathered(self):
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
        def _stop(current_task):
            for task in asyncio.Task.all_tasks():
                if task != current_task:
                    task.cancel()

        loop = asyncio.get_event_loop()

        try:
            # Causes the `gathered` event
            loop.run_until_complete(self.gathered())

            current_task = asyncio.ensure_future(
                asyncio.wait(asyncio.Task.all_tasks())
            )
            loop.call_later(3, _stop, current_task)
            loop.run_until_complete(current_task)
        finally:
            loop.close()
