"""
storage:core.eventers.storage
"""

import radiality


class Eventer(radiality.Eventer):
    """
    The `storage` eventer
    """

    @radiality.event
    def pong(self):
        pass
