"""
console:core.eventers.console
"""

import asyncio
import radiality


class Eventer(radiality.Eventer):
    """
    The `console` eventer
    """

    # event
    @asyncio.coroutine
    def ping(self):
        self.log('please stand by...')
        yield from asyncio.sleep(1)
        self.log('ping...')
        yield from self.actualize(event='ping')
