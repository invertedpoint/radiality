"""
radiality:radiality.ray

The `radiality/ray.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import re
import json

import requests

from radiality import utils


class Eventer:
    """
    Base class for eventers
    """
    # Subsystem ID and frequency
    sid = None  # TODO: Need to compute with `_subsystem_id`
    freq = None
    # Events and effectors
    _events = {}
    _effectors = []
    # Settings
    _url_protocol = None
    # Logging
    _logger = None

    def __init__(self, intf):
        """
        Initialization
        """
        self._url_protocol = intf.url_protocol
        self._logger = utils.Logger(configs_dir=intf.configs_dir).applog()

        intf.add_route('/spi/v1/ray', resource=self)

    def log(self, msg, *args, **kwargs):
        """
        Logs the info message
        """
        self._logger.info(msg, *args, **kwargs)

    def connect(self, sid, freq):
        """
        Connects the specified effector
        """
        if (sid, freq) not in self._effectors:
            self._effectors.append((sid, freq))

    def disconnect_effector(self):
        """
        Disconnects the specified effector
        """
        pass

    def create_event(self, event, data, rid=None):
        """
        Creates the specified event
        """
        if rid is None:  # => actualize the event immediately
            self._actualize(event, data)
        elif rid in self._events:
            raise NotImplementedError()
        # Otherwise => store the event
        self._events[rid] = (event, data)

    def release_event(self, rid):
        """
        Releases the stored event
        """
        if rid in self._events:
            (event, data) = self._events.pop(rid)
            self._actualize(event, data)

    def _actualize(self, event, data):
        """
        Actualizes the specified event
        """
        payload = {event: True}
        if data:
            payload.update(data)

        for (sid, freq) in self._effectors:
            resp = requests.get(
                url='{protocol}://{freq}/spi/v1/cell/{sid}'.format(
                    protocol=self._url_protocol, freq=freq, sid=self.sid
                ),
                params=payload
            )
            # Validates response
            # ...

    def _subsystem_id(self):
        """
        Returns the subsystem ID
        """
        headed = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', self.__class__.__name__)
        separated = re.sub('([a-z])([A-Z0-9])', r'\1-\2', headed)

        return separated.lower()
