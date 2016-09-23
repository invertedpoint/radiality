"""
console:core.subsystem
"""

import asyncio
import radiality

from core.eventers import console
from core.effectors import center
from core.effectors import storage


class Console(radiality.Subsystem):
    """
    The `console` subsystem
    """
    eventer = console.Eventer
    effectors = {
        'center': center.Effector,
        'storage': storage.Effector
    }

    # overridden from `radiality.Subsystem`
    @asyncio.coroutine
    def launched(self):
        yield from super().launched()

        channel = yield from self.connect(
            sid='center', freq='ws://127.0.0.1:50500'
        )
        yield from self.disconnect(sid='center', channel=channel)
