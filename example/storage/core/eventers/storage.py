"""
storage:core.eventers.storage
"""

import asyncio
import radiality


class Eventer(radiality.Eventer):
    """
    The `storage` eventer
    """

    # event
    @asyncio.coroutine
    def pong(self):
        yield from self.actualize(event='pong')
