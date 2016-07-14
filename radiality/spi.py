"""
radiality:radiality.spi

The `radiality/spi.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import falcon


class Subsystem(falcon.API):
    """
    Subsystem programming interface
    """
    eventer = None
    components = None

    _inst_eventer = None
    _inst_components = None

    def __init__(self):
        """
        Initialization
        """
        super().__init__(after=[cross_domain])

        if self.eventer:
            self._inst_eventer = self.eventer(intf=self)

            if self.components:
                self._inst_components = [
                    component(eventer=self._inst_eventer, intf=self)
                    for component in self.components
                ]

    def pulse(self, rid):
        """
        Pulsing
        """
        self._inst_eventer.release_event(rid)


def cross_domain(req, resp):
    """
    Enables the Cross-Origin Resource Sharing (CORS)
    """
    resp.set_header('Access-Control-Allow-Headers', 'Content-Type')
    resp.set_header(
        'Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS'
    )
    resp.set_header('Access-Control-Allow-Origin', '*')
