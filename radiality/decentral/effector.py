"""
radiality:radiality.decentral.effector

The `radiality/decentral/effector.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import asyncio

import websockets

from radiality.nonlinear.effector import AsyncEffector


class TeleEffector(AsyncEffector):
    _channel_host = None  # type: str
    _channel_port = None  # type: int

    def _effector_types():
        """
        return: Set[Type]

        Overridden from `AsyncEffector`.
        """
        return AsyncEffector._effector_types().union({TeleEffector})

    def channel_uri(self):
        """
        self: TeleEffector
        """
        (host, port) = (self._channel_host, self._channel_port)
        if isinstance(host, str) and isinstance(port, int):
            return '{scheme}://{host}:{port}'.format(
                scheme='ws', host=host, port=port
            )
        # Otherwise
        return None

    def sensor(self, host, port):
        """
        self: TeleEffector
        host: str
        port: int
        """
        if self._channel_host is None:
            self._channel_host = host

        if self._channel_port is None:
            self._channel_port = port

        if self._channel_host and self._channel_port:
            asyncio.get_event_loop().run_until_complete(
                websockets.serve(
                    self._tracing, self._channel_host, self._channel_port
                )
            )

        return self

    async def _tracing(self, channel, path):
        """
        self: TeleEffector
        channel: websockets.client.WebSocketClientProtocol
        path: str
        """
        try:
            while True:
                event_props = await channel.recv()
                await self.add_event(event_props)
        except websockets.exceptions.ConnectionClosed:
            # TODO: handle the error
            pass
        except asyncio.CancelledError:
            # TODO: handle the error
            pass
