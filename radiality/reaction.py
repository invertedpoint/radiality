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


class Effector(watch.Loggable, circuit.Connectable):
    """
    Receiver of the specific events
    """
    _eventer = None  # type: Eventer
    _effects = {}  # type: dict of str -> method
    _channel = None

    def __init__(self, logger, connector, eventer, channel):
        """
        Initialization
        """
        self._logger = logger
        self._connector = connector

        self._eventer = eventer
        self._channel = channel

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
            signal = yield from self._channel.recv()
            signal = json.loads(signal)
        except ConnectionClosed:
            self.warn('Connection closed')
        except ValueError:
            self.fail('Invalid in-signal -- could not decode the signal body')
        else:
            yield from self._parse(signal)
            return True

        return False

    @asyncio.coroutine
    def _connecting(self, channel):
        signal = {'event': 'connecting', 'sid': self.sid, 'freq': self.freq}

        try:
            signal = json.dumps(signal)
        except ValueError:
            self.fail('Invalid out-signal -- could not decode the signal body')
        else:
            try:
                yield from channel.send(signal)
            except ConnectionClosed:
                self.fail('Connection closed')

    @asyncio.coroutine
    def _parse(self, signal):
        event = signal.get('event', None)

        if event in self._effects:
            yield from self._effects[event](self, signal)
        elif event is None:
            self.fail('Invalid in-signal -- could not decode the signal body')
        else:
            self.warn('Unknown event -- {0}'.format(event))
