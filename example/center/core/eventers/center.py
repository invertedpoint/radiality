"""
center:core.eventers.center
"""

import asyncio
import radiality


class Eventer(radiality.Eventer):
    """
    The `center` eventer
    """
    _subsystems = {}

    # overridden from `radiality.Eventer`
    @asyncio.coroutine
    def effector_connected(self, sid, freq):
        yield from super().effector_connected(sid, freq)

        if sid not in self._subsystems:
            self._subsystems[sid] = freq

            yield from self.systemized(
                subsystems=list(self._subsystems.items())
            )

    # overridden from `radiality.Eventer`
    @asyncio.coroutine
    def effector_disconnected(self, sid):
        yield from super().effector_disconnected(sid)

        self._subsystems.pop(sid, None)

    @radiality.event
    def systemized(self, subsystems):
        self.log('systemized: %s', str(subsystems))
