"""
center:core.eventer
"""

import os

import asyncio
from radiality import Eventer
from radiality import utils


SELF_SID = 'center'
SELF_HOST = '127.0.0.1'
SELF_PORT = 50500
SELF_FREQ = utils.subsystem_freq(SELF_HOST, SELF_PORT)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')


class Center(Eventer):
    """
    The `center` eventer
    """
    sid = SELF_SID
    host = SELF_HOST
    port = SELF_PORT
    freq = SELF_FREQ

    subsystems = []

    logger = utils.Logger(configs_dir=CONFIGS_DIR).applog()

    # event
    @asyncio.coroutine
    def systemized(self):
        yield from self.actualize(
            event='systemized',
            data={'subsystems': self.subsystems}
        )
