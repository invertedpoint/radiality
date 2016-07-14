"""
radiality:radiality.api

The `radiality/api.py` is a part of `radiality`.
Apache 2.0 licensed.
"""


class Action:
    """
    Action of API
    """
    eventer = None
    route = None

    def __init__(self, eventer, intf):
        """
        Initialization
        """
        self.eventer = eventer

        if self.route:
            intf.add_route(self.route, resource=self)

    def log(self, msg, *args, **kwargs):
        """
        Logs the info message
        """
        self.eventer.log(msg, *args, **kwargs)
