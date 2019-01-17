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
    IS_ROUTES_RANDOMIZED = True
    MAX_CONN_SHOTS = 60
    RECONN_WAIT_TIME = 1  # 1 sec

    _cluster_routes: List[str]
    _connection: Client

    def connection(self) -> Client:
        """
        TODO: Add docstring
        """
        if not hasattr(self, '_connection'):
            self._connection = Client()

        return self._connection

    def cohere(self, scheme: str, host: str, port: int) -> Self:
        """
        TODO: Add docstring
        """
        self._cluster_routes = [f'{scheme}://{host}:{port}']

        asyncio.get_event_loop().run_until_complete(self._connect())

        return self

    async def connected(self) -> None:
        """
        TODO: Add docstring
        """
        url = self.connection().connected_url.netloc
        print(f'(i) Got connected to [{url}]')

    async def disconnected(self) -> None:
        """
        TODO: Add docstring
        """
        url = self.connection().connected_url.netloc
        print(f'(i) Got disconnected from [{url}]')

    async def reconnected(self) -> None:
        """
        TODO: Add docstring
        """
        url = self.connection().connected_url.netloc
        print(f'(i) Got reconnected to [{url}]')

    async def failed(self, error) -> None:
        """
        TODO: Add docstring
        """
        url = self.connection().connected_url.netloc
        print(f'(i) There was an error of connecting to [{url}]: {error}')

    async def closed(self) -> None:
        """
        TODO: Add docstring
        """
        print('(i) Connection is closed')

    async def _connect(self) -> None:
        """
        TODO: Add docstring
        """
        try:
            await self.connection().connect(
                servers=self._cluster_routes,
                loop=asyncio.get_event_loop(),
                dont_randomize=(not self.IS_ROUTES_RANDOMIZED),
                max_reconnect_attempts=self.MAX_CONN_SHOTS,
                reconnect_time_wait=self.RECONN_WAIT_TIME,
                disconnected_cb=self.disconnected,
                reconnected_cb=self.reconnected,
                error_cb=self.failed,
                closed_cb=self.closed
            )
        except errors.ErrNoServers as exc:
            print(f'(i) Could not connect to any server in the cluster: {exc}')
        else:
            await self.connected()
