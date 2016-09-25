"""
console:core.effectors.center
"""

import asyncio
import radiality


class Effector(radiality.Effector):
    """
    Effector for the handling of events of the `center` subsystem
    """

    def __new__(cls, *args, **kwargs):
        """
        Pre-initialization
        """
        cls._effects = {
            'systemized': cls.systemized
        }

        return super().__new__(cls, *args, **kwargs)

    # effect
    @asyncio.coroutine
    def systemized(self, signal):
        subsystems = signal.get('subsystems', [])

        for (sid, freq) in subsystems:
            if sid in self.wanted:
                yield from self.connect(sid, freq)

                if sid == 'storage':
                    yield from self._eventer.ping()
