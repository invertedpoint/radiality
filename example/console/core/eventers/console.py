"""
console:core.eventers.console
"""

import asyncio
import radiality


class Eventer(radiality.Eventer):
    """
    The `console` eventer
    """

    @radiality.event
    def ping(self):
        self.log('please stand by...')
        yield from asyncio.sleep(1)
        self.log('ping...')
