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
            event=method.__name__, details=(kwargs or None)
        )

    _wrapper._is_event = True

    return asyncio.coroutine(_wrapper)


class Eventer(watch.Loggable, circuit.Connectable):
    """
    Emitter of the specific events
    """
    _effectors = None

    def __init__(self, logger, connector):
        """
        Initialization
        """
        self._logger = logger
        self._connector = connector

        self._effectors = {}

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
        yield from self.effector_disconnected(sid)

    def register_effector(self, sid, channel):
        self._effectors[sid] = channel

    @asyncio.coroutine
    def effector_connected(self, sid, freq):
        data = {
            '*signal': ('biconnected' if sid in self.wanted else 'connected'),
            'sid': self.sid,
            'freq': self.freq
        }

        try:
            data = json.dumps(data)
            yield from self._effectors[sid].send(data)
        except ValueError:
            self.fail('Invalid output -- could not decode data: %s', str(data))
        except ConnectionClosed:
            self.fail('Connection closed')

    @asyncio.coroutine
    def effector_disconnected(self, sid):
        pass

    @asyncio.coroutine
    def _transmit(self, signal, channel, details=None):
        data = {'*signal': signal}
        if details:
            data.update(details)

        try:
            data = json.dumps(data)
            yield from channel.send(data)
        except ValueError:
            self.fail('Invalid output -- could not decode data: %s', str(data))
        except ConnectionClosed:
            self.fail('Connection closed')
        else:
            return True

        return False

    @asyncio.coroutine
    def _actualize(self, event, details=None):
        data = {'*event': event}
        if details:
            data.update(details)

        try:
            data = json.dumps(data)
        except ValueError:
            self.fail('Invalid output -- could not decode data: %s', str(data))
        else:
            for (sid, channel) in list(self._effectors.items()):
                try:
                    yield from channel.send(data)
                except ConnectionClosed:
                    self.warn('Connection to `%s` closed', sid)
                    # Clears the wasted effector
                    self._effectors.pop(sid)
                    yield from self.effector_disconnected(sid)
