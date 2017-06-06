"""
radiality:radiality.decentral.eventer

The `radiality/decentral/eventer.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import asyncio

import websockets

from radiality.nonlinear.eventer import AsyncEventer
from radiality.nonlinear.effect import async_effect
from radiality.decentral.effector import TeleEffector


class TeleRing(TeleEffector):

    @async_effect
    async def systemized(self, channels_uris):
        """
        self: TeleEventer
        channels_uris: Dict[str, List[str]]
        """
        if self.CORE_ID in channels_uris:
            for channel_uri in channels_uris[self.CORE_ID]:
                await self._focus_channel(channel_uri)


class TeleEventer(AsyncEventer, TeleRing):
    MAX_CONN_SHOTS = 60
    RECONN_WAIT_TIME = 1  # 1 sec

    _channels = None  # type: Dict[str,
    #                              websockets.client.WebSocketClientProtocol]

    def _eventer_type():
        """
        return: Type

        Overridden from `SyncEventer`.
        """
        return TeleEventer

    def __init__(self):
        """
        self: TeleEventer
        """
        super().__init__()

        self._channels = {}

    async def _focus_channel(self, channel_uri):
        """
        self: TeleEventer
        channel_uri: str
        """
        channel = self._channels.get(channel_uri, None)

        if not (channel and channel.open):
            channel = await self._channel(channel_uri)

            if channel is None:  # => critical fail
                # TODO: logging the error
                pass
            else:
                self._channels[channel_uri] = channel

    async def _channel(self, channel_uri):
        """
        self: TeleEventer
        channel_uri: str
        """
        channel = None
        conn_shot = 0

        while (channel is None) and (conn_shot < self.MAX_CONN_SHOTS):
            try:
                channel = await websockets.connect(channel_uri)
            except Exception as exc:
                conn_shot += 1
                # TODO: logging the shot
                print('Shot {0}'.format(conn_shot))
                await asyncio.sleep(self.RECONN_WAIT_TIME)

        return channel

    def _actualization_tasks(self, event_props):
        """
        self: TeleEventer
        event_props: Dict[str, Any]

        return: List[asyncio.Task]

        Overridden from `AsyncEffector`.
        """
        return super()._actualization_tasks(event_props) + [
            asyncio.ensure_future(channel.send(event_props))
            for channel in self._channels.values()
        ]
