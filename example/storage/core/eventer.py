"""
storage:core.eventer
"""

import asyncio
from radiality import Eventer
from radiality import utils


SELF_SID = 'storage'
SELF_HOST = 'storage'
SELF_PORT = 8888
SELF_FREQ = utils.subsystem_freq(SELF_HOST, SELF_PORT)


class Storage(Eventer):
    """
    The `storage` eventer
    """
    sid = SELF_SID
    host = SELF_HOST
    port = SELF_PORT
    freq = SELF_FREQ

    wanted = ['center', 'console']

    # event
    @asyncio.coroutine
    def pong(self):
        yield from self.actualize(event='pong')
