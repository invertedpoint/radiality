"""
console:core.effectors.storage
"""

import asyncio
import radiality


class Effector(radiality.Effector):
    """
    Effector for the handling of events of the `storage` subsystem
    """

    def __new__(cls, *args, **kwargs):
        """
        Pre-initialization
        """
        cls._effects = {
            'pong': cls.pong
        }

        return super().__new__(cls, *args, **kwargs)

    # effect
    @asyncio.coroutine
    def pong(self, signal):
        self.log('Storage -> pong')
