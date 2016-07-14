"""
console:core.actions
"""

import json

from radiality import Action


class Sample(Action):
    """
    Action of the Sample API
    """
    route = '/api/v1/sample'

    def on_get(self, req, resp):
        """
        Handles of the `GET` requests:
            * `/api/v1/sample/`
        """
        self.eventer.data_sampling(rid=req.get_param('rid'))

        resp.body = json.dumps({'data': None, 'error': False, 'msg': ''})
