"""
storage:core.effectors
"""

import json

from radiality import Effector


class Center(Effector):
    """
    Effector for the handling of events of the `center` subsystem
    """
    sid = 'center'

    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        super().__init__(*args, **kwargs)

        self.connect(freq='center:8888')

    def on_get(self, req, resp):
        """
        Handles of the `GET` requests:
            * `/spi/v1/cell/center/:subsystem_ready`
        """
        if req.get_param('subsystem_ready'):
            self.subsystem_ready(subsystems=req.params)

        resp.body = json.dumps({'data': None, 'error': False, 'msg': ''})

    def subsystem_ready(self, subsystems):
        """
        Effect
        """
        if 'console' in subsystems:
            self.connect(freq=subsystems['console'])


class Console(Effector):
    """
    Effector for the handling of events of the `console` subsystem
    """
    sid = 'console'

    def on_get(self, req, resp):
        """
        Handles of the `GET` requests:
            * `/spi/v1/cell/console/:data_sampling`
        """
        if req.get_param('data_sampling'):
            self.data_sampling(rid=req.get_param('rid'))

        resp.body = json.dumps({'data': None, 'error': False, 'msg': ''})

    def data_sampling(self, rid):
        """
        Effect
        """
        self.log('storage:core.cells.Console.data_sampling')

        self.eventer.data_sampled(rid)
