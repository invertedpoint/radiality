"""
radiality:radiality.reaction

The `radiality/reaction.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import json

import asyncio
from websockets.exceptions import ConnectionClosed

import utils


class Effector:
    eventer = None
    effects = {}
    _channel = None

    def __init__(self, eventer, channel):
        self.eventer = eventer
        self._channel = channel

    @asyncio.coroutine
    def activate(self):
        try:
            signal = yield from self._channel.recv()
            signal = json.loads(signal)
        except ConnectionClosed:
            utils.fail_connection()
        except ValueError:
            utils.fail_in_signal()
        else:
            yield from self.parse(signal)
            return True

        return False

    @asyncio.coroutine
    def parse(self, signal):
        event = signal.get('event', None)

        if event == 'connected':
            yield from self.connected(signal)
        elif event in self.effects:
            yield from self.effects[event](self, signal)
        elif event is None:
            utils.fail_in_signal()
        else:
            utils.fail_event(event)

    # effect
    @asyncio.coroutine
    def connected(self, signal):
        """
        Subsystem connected
        """
        sid = signal.get('sid', None)
        freq = signal.get('freq', None)
        wanted = signal.get('wanted', [])

        if sid and freq:
            if sid in self.eventer.wanted:
                self.eventer.wanted.remove(sid)

            if self.eventer.sid in wanted:
                yield from self.eventer.connect(sid, freq)

                channel = self.eventer.effectors.get(sid, None)
                if channel:
                    self._channel = channel
                    yield from self.eventer.connected(sid)
            elif sid in self.eventer.effectors:
                yield from self.eventer.disconnect(sid)
                self.eventer.effectors[sid] = self._channel
