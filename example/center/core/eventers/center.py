"""
center:core.eventers.center
"""

import asyncio
import radiality


class Eventer(radiality.Eventer):
    """
    The `center` eventer
    """
    _subsystems = []

    # overridden from `radiality.Eventer`
    @asyncio.coroutine
    def effector_connected(self, sid, freq):
        yield from super().effector_connected(sid, freq)

        if (sid, freq) not in self._subsystems:
            self._subsystems.append((sid, freq))

            yield from self.systemized(subsystems=self._subsystems)

    # event
    @asyncio.coroutine
    def systemized(self, subsystems):
        yield from self.actualize(
            event='systemized', data={'subsystems': subsystems}
        )
