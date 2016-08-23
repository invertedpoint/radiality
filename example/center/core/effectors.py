"""
center:core.effectors
"""

import asyncio
from radiality import Effector


class Subsystem(Effector):
    """
    Effector for the handling of events of all subsystems
    """

    # default effect
    @asyncio.coroutine
    def connected(self, signal):
        sid = signal.get('sid', None)
        freq = signal.get('freq', None)
        wanted = signal.get('wanted', [])

        yield from self.eventer.connect(sid, freq)
        yield from self.eventer.connected(sid)

        self.eventer.subsystems.append((sid, freq, wanted))
        yield from self.eventer.systemized()
