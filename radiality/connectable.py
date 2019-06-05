"""
radiality:radiality.connectable

The `radiality/connectable.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from typing import TypeVar
from typing import List
import json
import asyncio

from nats.aio.client import Client
from nats.aio import errors


Self = TypeVar('Self', bound='Connectable')


class Connectable:
    """
    TODO: Add docstring
    """
    _IS_ROUTES_RANDOMIZED_ = True
    _MAX_CONN_SHOTS_ = 60
    _RECONN_WAIT_TIME_ = 1  # 1 sec

    _cluster_routes_: List[str]
    _connection_: Client

    def cohere(self, scheme: str, host: str, port: int) -> Self:
        """
        TODO: Add docstring
        """
        self._cluster_routes_ = [f'{scheme}://{host}:{port}']

        asyncio.get_event_loop().run_until_complete(self._connect_())

        return self

    async def _connected_(self) -> None:
        """
        TODO: Add docstring
        """
        url = self._connection_.connected_url.netloc
        print(f'(i) Got connected to [{url}]')

    async def _disconnected_(self) -> None:
        """
        TODO: Add docstring
        """
        url = self._connection_.connected_url.netloc
        print(f'(i) Got disconnected from [{url}]')

    async def _reconnected_(self) -> None:
        """
        TODO: Add docstring
        """
        url = self._connection_.connected_url.netloc
        print(f'(i) Got reconnected to [{url}]')

    async def _failed_(self, error) -> None:
        """
        TODO: Add docstring
        """
        url = self._connection_.connected_url.netloc
        print(f'(i) There was an error of connecting to [{url}]: {error}')

    async def _closed_(self) -> None:
        """
        TODO: Add docstring
        """
        print('(i) Connection is closed')

    async def _connect_(self) -> None:
        """
        TODO: Add docstring
        """
        if not hasattr(self, '_connection_'):
            self._connection_ = Client()

        try:
            await self._connection_.connect(
                servers=self._cluster_routes_,
                loop=asyncio.get_event_loop(),
                dont_randomize=(not self._IS_ROUTES_RANDOMIZED_),
                max_reconnect_attempts=self._MAX_CONN_SHOTS_,
                reconnect_time_wait=self._RECONN_WAIT_TIME_,
                disconnected_cb=self._disconnected_,
                reconnected_cb=self._reconnected_,
                error_cb=self._failed_,
                closed_cb=self._closed_
            )
        except errors.ErrNoServers as exc:
            print(f'(i) Could not connect to any server in the cluster: {exc}')
        else:
            await self._connected_()
