"""
radiality:radiality.creation

The `radiality/creation.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import json

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

from radiality import utils


class Eventer(utils.Loggable):
    """
    Emitter of the specific events
    """
    configs_dir = None

    sid = None
    freq = None
    wanted = []

    _effectors = {}

    def __init__(self):
        """
        Initialization
        """
        self._logger = utils.Logger(configs_dir=self.configs_dir).applog()

    @asyncio.coroutine
    def connect(self, sid, freq):
        while True:
            try:
                channel = yield from websockets.connect(freq + '/' + self.sid)
            except ConnectionClosed:
                self.warn('Connection closed')
                yield from asyncio.sleep(1)
            else:
                self._effectors[sid] = channel
                break

    @asyncio.coroutine
    def disconnect(self, sid):
        channel = self._effectors.pop(sid)

        try:
            yield from channel.close()
        except ConnectionClosed:
            self.warn('Connection closed')
        finally:
            del channel

    @asyncio.coroutine
    def actualize(self, event, data=None, sid=None):
        signal = {'event': event}
        if data:
            signal.update(data)

        try:
            signal = json.dumps(signal)
        except ValueError:
            self.fail('Invalid out-signal -- could not decode the signal body')
        else:
            if sid:
                try:
                    yield from self._effectors[sid].send(signal)
                except ConnectionClosed:
                    self.warn('Connection closed')
                    # Clears the wasted effector
                    self._effectors.pop(sid)
            else:
                for (sid, channel) in list(self._effectors.items()):
                    try:
                        yield from channel.send(signal)
                    except ConnectionClosed:
                        self.warn('Connection closed')
                        # Clears the wasted effector
                        self._effectors.pop(sid)

    # event
    @asyncio.coroutine
    def connected(self, sid):
        yield from self.actualize(
            event='connected',
            data={'sid': self.sid, 'freq': self.freq, 'wanted': self.wanted},
            sid=sid
        )
