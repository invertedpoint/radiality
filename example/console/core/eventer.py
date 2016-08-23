"""
console:core.eventer
"""

import asyncio
from radiality import Eventer
from radiality import utils


SELF_SID = 'console'
SELF_HOST = 'console'
SELF_PORT = 8888
SELF_FREQ = utils.subsystem_freq(SELF_HOST, SELF_PORT)


class Console(Eventer):
    """
    The `console` eventer
    """
    sid = SELF_SID
    host = SELF_HOST
    port = SELF_PORT
    freq = SELF_FREQ

    wanted = ['center', 'storage']

    # event
    @asyncio.coroutine
    def ping(self):
        print('ping...')
        yield from self.actualize(event='ping')
