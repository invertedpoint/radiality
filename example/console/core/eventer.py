"""
console:core.eventer
"""

import json

from radiality import Eventer


class Console(Eventer):
    """
    The `console` eventer
    """
    sid = 'console'
    freq = 'console:8888'

    def on_get(self, req, resp):
        """
        Handles of the `GET` requests:
            * `/spi/v1/ray/:sid:freq`
        """
        sid = req.get_param('sid')
        freq = req.get_param('freq')

        if sid and freq:
            # Connecting
            self.connect(sid, freq)

        resp.body = json.dumps({'data': None, 'error': False, 'msg': ''})

    def data_sampling(self, rid):
        """
        Event
        """
        self.log('console:core.rays.Console.data_sampling')

        self.create_event(event='data_sampling', data=None, rid=rid)
