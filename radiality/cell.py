"""
radiality:radiality.cell

The `radiality/cell.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import re
import json

import requests
from requests.exceptions import RequestException

from radiality import utils


class Effector:
    """
    Base class for effectors
    """
    # Subsystem ID
    sid = None  # TODO: Need to compute with `_subsystem_id`
    # Eventer
    eventer = None

    def __init__(self, eventer, intf):
        """
        Initialization
        """
        self.eventer = eventer
        intf.add_route(
            '/spi/v1/cell/{sid}'.format(sid=self.sid), resource=self
        )

    def log(self, msg, *args, **kwargs):
        """
        Logs the info message
        """
        self.eventer.log(msg, *args, **kwargs)

    def connect(self, freq):
        """
        Connects to the corresponding `eventer`
        """
        probing = True
        while probing:
            try:
                resp = requests.get(
                    url='{protocol}://{freq}/spi/v1/ray'.format(
                        protocol=utils.URL_PROTOCOL, freq=freq
                    ),
                    params={
                        'sid': self.eventer.sid,
                        'freq': self.eventer.freq
                    }
                )
                probing = False
                # Validates response
                # ...
            except RequestException as exc:
                pass

    def _subsystem_id(self):
        """
        Returns the subsystem ID
        """
        headed = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', self.__class__.__name__)
        separated = re.sub('([a-z])([A-Z0-9])', r'\1-\2', headed)

        return separated.lower()
