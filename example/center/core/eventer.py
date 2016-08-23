"""
center:core.eventer
"""

import asyncio
from radiality import Eventer
from radiality import utils


SELF_SID = 'center'
SELF_HOST = 'center'
SELF_PORT = 8888
SELF_FREQ = utils.subsystem_freq(SELF_HOST, SELF_PORT)


class Center(Eventer):
    """
    The `center` eventer
    """
    sid = SELF_SID
    host = SELF_HOST
    port = SELF_PORT
    freq = SELF_FREQ

    subsystems = []

    # event
    @asyncio.coroutine
    def systemized(self):
        yield from self.actualize(
            event='systemized',
            data={'subsystems': self.subsystems}
        )
