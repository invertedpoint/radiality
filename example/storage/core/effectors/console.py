"""
storage:core.effectors.console
"""

import asyncio
import radiality


class Effector(radiality.Effector):
    """
    Effector for the handling of events of the `console` subsystem
    """

    def __new__(cls, *args, **kwargs):
        """
        Pre-initialization
        """
        cls._effects = {
            'ping': cls.ping
        }

        return super().__new__(cls, *args, **kwargs)

    # effect
    @asyncio.coroutine
    def ping(self, signal):
        self.log('Console -> ping')
        yield from self._eventer.pong()
