"""
radiality:examples:simple:poly:family.core
"""

import asyncio

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
