"""
radiality:radiality.creation

The `radiality/creation.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from functools import wraps
import json

import asyncio
from websockets.exceptions import ConnectionClosed

from radiality import watch
from radiality import circuit


def event(method):
    """
    Decorator for the definition of an event
    """
    method = asyncio.coroutine(method)

    @wraps(method)
    def _wrapper(self, **kwargs):
        yield from method(self, **kwargs)
        yield from self._actualize(
            event=method.__name__, data=(kwargs or None)
        )

    _wrapper._is_event = True

    return asyncio.coroutine(_wrapper)


class Eventer(watch.Loggable, circuit.Connectable):
    """
    Emitter of the specific events
    """
    _effectors = {}

    def __init__(self, logger, connector):
        """
        Initialization
        """
        self._logger = logger
        self._connector = connector

    # overridden from `circuit.Connectable`
    @asyncio.coroutine
    def connect(self, sid, freq):
        if sid in self._effectors:  # => reconnect
            yield from self.disconnect(sid, channel=None)

        channel = yield from super().connect(sid, freq)
        if channel:  # => register a new effector
            self.register_effector(sid, channel)
            yield from self.effector_connected(sid, freq)

        return channel

    # overridden from `circuit.Connectable`
    @asyncio.coroutine
    def disconnect(self, sid, channel):
        channel = self._effectors.pop(sid, channel)
        yield from super().disconnect(sid, channel)

    def register_effector(self, sid, channel):
        self._effectors[sid] = channel

    @asyncio.coroutine
    def effector_connected(self, sid, freq):
        signal = {
            'event': ('biconnected' if sid in self.wanted else 'connected'),
            'sid': self.sid,
            'freq': self.freq
        }

        try:
            signal = json.dumps(signal)
        except ValueError:
            self.fail('Invalid out-signal -- could not decode the signal body')
        else:
            try:
                yield from self._effectors[sid].send(signal)
            except ConnectionClosed:
                self.fail('Connection closed')

    @asyncio.coroutine
    def _actualize(self, event, data=None):
        signal = {'event': event}
        if data:
            signal.update(data)

        try:
            signal = json.dumps(signal)
        except ValueError:
            self.fail('Invalid out-signal -- could not decode the signal body')
        else:
            for (sid, channel) in list(self._effectors.items()):
                try:
                    yield from channel.send(signal)
                except ConnectionClosed:
                    self.warn('Connection closed')
                    # Clears the wasted effector
                    self._effectors.pop(sid)
