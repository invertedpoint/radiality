"""
radiality:radiality.eventer

The `radiality/eventer.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from typing import TypeVar
from typing import Dict
from typing import Any
import json
import asyncio

from nats.aio import errors

from radiality.connectable import Connectable


Self = TypeVar('Self', bound='Eventer')


class Eventer(Connectable):
    """
    TODO: Add docstring
    """
    _CORE_ID_: str

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        """
        TODO: Add docstring
        """
        if not hasattr(cls, '_CORE_ID_'):
            eventer_cls = Eventer
            core_ids = [
                base_cls.__name__
                for base_cls in cls.__mro__
                if eventer_cls in base_cls.__bases__
            ]

            if len(core_ids) == 1:
                cls._CORE_ID_ = core_ids[0]
            else:
                # TODO: handle the error
                pass

        return super().__new__(cls)

    async def _actualize_(
        self, event_id: str, event_props: Dict[str, Any]
    ) -> None:
        """
        TODO: Add docstring
        """
        event_path = f'{self._CORE_ID_}.{event_id}'

        try:
            event_payload = json.dumps(event_props)
        except ValueError:
            # TODO: handle the error
            pass
        else:
            await self._publish_(event_path, event_payload)

    async def _publish_(self, event_path: str, event_payload: str) -> None:
        """
        TODO: Add docstring
        """
        try:
            await self._connection_.publish(
                event_path, event_payload.encode()
            )
        except errors.ErrConnectionClosed as exc:
            print(f'(i) Connection closed prematurely: {exc}')
        except errors.ErrTimeout as exc:
            print(
                f'(i) Timeout occured when publishing "{event_path}": {exc}'
            )
