"""
storage:core.subsystem
"""

import asyncio
import radiality

from core.eventers import storage
from core.effectors import center
from core.effectors import console


class Storage(radiality.Subsystem):
    """
    The `storage` subsystem
    """
    eventer = storage.Eventer
    effectors = {
        'center': center.Effector,
        'console': console.Effector
    }

    # overridden from `radiality.Subsystem`
    @asyncio.coroutine
    def launched(self):
        yield from super().launched()

        yield from self.connect(sid='center', freq='ws://127.0.0.1:50500')
