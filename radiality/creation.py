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


class Eventer:
    effectors = {}

    sid = None
    freq = None
    wanted = []

    @asyncio.coroutine
    def connect(self, sid, freq):
        while True:
            try:
                channel = yield from websockets.connect(freq + '/' + self.sid)
            except ConnectionClosed:
                utils.fail_connection()
                yield from asyncio.sleep(1)
            else:
                self.effectors[sid] = channel
                break

    @asyncio.coroutine
    def disconnect(self, sid):
        channel = self.effectors.pop(sid)

        try:
            yield from channel.close()
        except ConnectionClosed:
            utils.fail_connection()
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
            utils.fail_out_signal()
        else:
            if sid:
                try:
                    yield from self.effectors[sid].send(signal)
                except ConnectionClosed:
                    utils.fail_connection()
            else:
                for (sid, channel) in self.effectors.items():
                    try:
                        yield from channel.send(signal)
                    except ConnectionClosed:
                        utils.fail_connection()

    # event
    @asyncio.coroutine
    def connected(self, sid):
        yield from self.actualize(
            event='connected',
            data={'sid': self.sid, 'freq': self.freq, 'wanted': self.wanted},
            sid=sid
        )
