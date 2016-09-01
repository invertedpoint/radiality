"""
storage:core.effectors
"""

import asyncio
from radiality import Effector


class Center(Effector):
    """
    Effector for the handling of events of the `center` subsystem
    """

    def __new__(cls, *args, **kwargs):
        """
        Pre-initialization
        """
        cls.effects = {
            'systemized': cls.systemized
        }

        return super().__new__(cls, *args, **kwargs)

    # default effect
    @asyncio.coroutine
    def connected(self, signal):
        sid = signal.get('sid', None)
        if sid:
            self.eventer.wanted.remove(sid)
            yield from self.eventer.disconnect(sid)

    # effect
    @asyncio.coroutine
    def systemized(self, signal):
        subsystems = signal.get('subsystems', [])

        for (sid, freq, wanted) in subsystems:
            if self.eventer.sid in wanted:
                yield from self.eventer.connect(sid, freq)
                yield from self.eventer.connected(sid)


class Console(Effector):
    """
    Effector for the handling of events of the `console` subsystem
    """

    def __new__(cls, *args, **kwargs):
        """
        Pre-initialization
        """
        cls.effects = {
            'ping': cls.ping
        }

        return super().__new__(cls, *args, **kwargs)

    # effect
    @asyncio.coroutine
    def ping(self, signal):
        self.eventer.logger.info('Console -> ping')
        yield from self.eventer.pong()
