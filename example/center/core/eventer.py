"""
center:core.eventer
"""

import json

from radiality import Eventer


class Center(Eventer):
    """
    The `center` eventer
    """
    sid = 'center'
    freq = 'center:8888'

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
            self.subsystem_ready(rid=req.get_param('rid'))

        resp.body = json.dumps({'data': None, 'error': False, 'msg': ''})

    def subsystem_ready(self, rid):
        """
        Event
        """
        self.create_event(
            event='subsystem_ready',
            data={sid: freq for (sid, freq) in self._effectors},
            rid=rid
        )
