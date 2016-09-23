"""
console:core.eventers.console
"""

import asyncio
import radiality


class Eventer(radiality.Eventer):
    """
    The `console` eventer
    """

    # overridden from `radiality.Eventer`
    @asyncio.coroutine
    def effector_connected(self, sid, freq):
        yield from super().effector_connected(sid, freq)

        if sid == 'storage':
            yield from self.ping()

    # event
    @asyncio.coroutine
    def ping(self):
        self.log('please stand by...')
        yield from asyncio.sleep(1)
        self.log('ping...')
        yield from self.actualize(event='ping')
