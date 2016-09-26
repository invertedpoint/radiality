"""
console:core.effectors.storage
"""

import radiality


class Effector(radiality.Effector):
    """
    Effector for the handling of events of the `storage` subsystem
    """

    @radiality.effect
    def pong(self, signal):
        self.log('Storage -> pong')
