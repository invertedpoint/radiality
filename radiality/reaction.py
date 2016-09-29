"""
radiality:radiality.reaction

The `radiality/reaction.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import json

import asyncio
from websockets.exceptions import ConnectionClosed

from radiality import watch
from radiality import circuit


def effect(method):
    """
    Decorator for the definition of an effect
    """
    method._is_effect = True

    return asyncio.coroutine(method)


class Effector(watch.Loggable, circuit.Connectable):
    """
    Receiver of the specific events
    """
    _eventer = None  # type: Eventer
    _channel = None  # type: WebSocketServerProtocol

    _effects = {}  # type: dict of str -> method

    def __new__(cls, *args, **kwargs):
        """
        Pre-initialization
        """
        for (name, method) in cls.__dict__.items():
            if getattr(method, '_is_effect', False):
                cls._effects[name] = method

        return super().__new__(cls, *args, **kwargs)

    def __init__(self, logger, connector, eventer, channel):
        """
        Initialization
        """
        self._logger = logger
        self._connector = connector

        self._eventer = eventer
        self._channel = channel

    @property
    def eventer(self):
        return self._eventer

    # overridden from `circuit.Connectable`
    @asyncio.coroutine
    def connect(self, sid, freq):
        channel = yield from super().connect(sid, freq)
        if channel:
            yield from self._connecting(channel)

        return channel

    @asyncio.coroutine
    def activate(self):
        try:
            data = yield from self._channel.recv()
            data = json.loads(data)
        except ConnectionClosed:
            self.warn('Connection closed')
        except ValueError:
            self.fail('Invalid input -- could not decode data: %s', str(data))
        else:
            yield from self._parse(data)
            return True

        return False

    @asyncio.coroutine
    def _connecting(self, channel):
        data = {'*signal': 'connecting', 'sid': self.sid, 'freq': self.freq}

        try:
            data = json.dumps(data)
            yield from channel.send(data)
        except ValueError:
            self.fail('Invalid output -- could not decode data: %s', str(data))
        except ConnectionClosed:
            self.fail('Connection closed')

    @asyncio.coroutine
    def _parse(self, data):
        event = data.get('*event', None)

        if event in self._effects:
            yield from self._effects[event](self, data)
        elif event is None:
            self.fail('Invalid input -- could not decode data: %s', str(data))
        else:
            self.warn('Unknown event -- {0}'.format(event))
