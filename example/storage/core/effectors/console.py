"""
storage:core.effectors.console
"""

import radiality


class Effector(radiality.Effector):
    """
    Effector for the handling of events of the `console` subsystem
    """

    @radiality.effect
    def ping(self, signal):
        self.log('Console -> ping')
        yield from self.eventer.pong()
