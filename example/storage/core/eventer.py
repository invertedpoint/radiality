"""
storage:core.eventer
"""

import json

from radiality import Eventer


class Storage(Eventer):
    """
    The `storage` eventer
    """
    sid = 'storage'
    freq = 'storage:8888'

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

    def data_sampled(self, rid):
        """
        Event
        """
        self.log('storage:core.rays.Storage.data_sampled')

        self.create_event(event='data_sampled', data=None, rid=rid)
