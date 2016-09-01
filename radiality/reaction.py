"""
radiality:radiality.reaction

The `radiality/reaction.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import json

import asyncio
from websockets.exceptions import ConnectionClosed

from radiality import utils


class Effector(utils.Loggable):
    """
    Receiver of the specific events
    """
    eventer = None
    effects = {}
    _channel = None

    def __init__(self, eventer, channel):
        """
        Initialization
        """
        self.eventer = eventer
        self._logger = self.eventer._logger
        self._channel = channel

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
            self.fail('Invalid in-signal -- could not decode the signal body')
        else:
            self.warn('Unknown event -- {0}'.format(event))

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

                channel = self.eventer._effectors.get(sid, None)
                if channel:
                    self._channel = channel
                    yield from self.eventer.connected(sid)
            elif sid in self.eventer._effectors:
                yield from self.eventer.disconnect(sid)
                self.eventer._effectors[sid] = self._channel
