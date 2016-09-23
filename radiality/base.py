"""
radiality:radiality.base

The `radiality/base.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import json

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

from radiality.reaction import Effector
from radiality import watch
from radiality import circuit


class Subsystem(watch.Loggable, circuit.Connectable):
    """
    Subsystem components container
    """
    logger_name = 'core.app'

    eventer = None  # default eventer, type: class
    effector = Effector  # default effector, type: class
    effectors = {}  # type: dict of str -> class

    _eventer_inst = None  # type: Eventer

    def __init__(self, logging_config, connection_config):
        """
        Initialization
        """
        self._logger = watch.Logger(
            config_path=logging_config, name=self.logger_name
        )
        self._connector = circuit.Connector(
            logger=self._logger,
            config_path=connection_config,
            wanted=self.effectors.keys()
        )

        if self.eventer:
            self._eventer_inst = self.eventer(
                logger=self._logger, connector=self._connector
            )
        else:
            raise Exception(
                'The `eventer` for the `{0}` subsystem '
                'is not specified'.format(self.sid)
            )

    def launch(self):
        """
        Launches the subsystem
        """
        event_loop = asyncio.get_event_loop()

        try:
            serving = websockets.serve(
                ws_handler=self._receiver,
                host=self.host,
                port=self.port
            )
            event_loop.run_until_complete(serving)

            event_loop.run_until_complete(self.launched())

            event_loop.run_forever()
        finally:
            event_loop.close()

    # overridden from `circuit.Connectable`
    @asyncio.coroutine
    def connect(self, sid, freq):
        effector_inst = Effector(
            logger=self._logger,
            connector=self._connector,
            eventer=self._eventer_inst,
            channel=None
        )
        channel = yield from effector_inst.connect(sid, freq)

        return channel

    @asyncio.coroutine
    def launched(self):
        self.log('Serving on `{0}`'.format(self.freq))

    @asyncio.coroutine
    def _receiver(self, channel, path):
        try:
            signal = yield from channel.recv()
        except ConnectionClosed:
            self.fail('Connection closed')
        else:
            try:
                signal = json.loads(signal)
            except ValueError:
                self.fail(
                    'Invalid in-signal -- could not decode the signal body'
                )
            else:
                yield from self._parse(signal, channel)

    @asyncio.coroutine
    def _parse(self, signal, channel):
        event = signal.get('event', None)
        sid = signal.get('sid', None)

        if event == 'connecting':
            freq = signal.get('freq', None)
            channel = yield from self._eventer_inst.connect(sid, freq)
        elif event == 'connected':
            self.log('Connected to `%s`', sid)
        elif event == 'biconnected':
            self.log('Biconnected to `%s`', sid)
            self._eventer_inst.register_effector(sid, channel)
        elif event is None:
            self.fail('Invalid in-signal -- could not decode the signal body')
        else:
            self.warn('Unknown event -- {0}'.format(event))

        if sid in self.wanted:
            self.unwanted(sid)
            yield from self._receiving(sid, channel)

    @asyncio.coroutine
    def _receiving(self, sid, channel):
        self.log('Receiving the `%s` subsystem', sid)

        effector_inst = self.effectors.get(sid, self.effector)(
            logger=self._logger,
            connector=self._connector,
            eventer=self._eventer_inst,
            channel=channel
        )

        receiving = True
        while receiving:
            receiving = yield from effector_inst.activate()
