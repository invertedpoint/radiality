"""
radiality:radiality.effector

The `radiality/effector.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from typing import TypeVar
from typing import Dict
from typing import Type
from typing import Callable
from typing import Any
import json
import asyncio

from nats.aio import errors

from radiality.connectable import Connectable


Self = TypeVar('Self', bound='Effector')


class Effector(Connectable):
    """
    TODO: Add docstring
    """
    _WANTED_: Dict[str, Type]
    _EFFECTS_: Dict[str, Callable[..., None]]

    _events_: asyncio.Queue
    _impactor_: asyncio.Task

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        """
        TODO: Add docstring
        """
        if not hasattr(cls, '_WANTED_'):
            effector_types = {Effector}
            cls._WANTED_ = {
                base_cls.__name__: base_cls
                for base_cls in cls.__mro__
                if (base_cls not in effector_types) and (
                    len(effector_types.intersection(base_cls.__bases__)) > 0
                )
            }

        if not hasattr(cls, '_EFFECTS_'):
            cls._EFFECTS_ = {
                ref.__qualname__: ref
                for effector_cls in cls._WANTED_.values()
                for ref in effector_cls.__dict__.values()
                if getattr(ref, '_IS_EFFECT_', False)
            }

        return super().__new__(cls)

    def __init__(self) -> None:
        """
        TODO: Add docstring
        """
        super().__init__()

        if not hasattr(self, '_events_'):
            self._events_ = asyncio.Queue()

        if not hasattr(self, '_impactor_'):
            self._impactor_ = asyncio.ensure_future(self._impacting_())

    async def _connected_(self) -> None:
        """
        TODO: Add docstring
        """
        await super()._connected_()

        if hasattr(self, '_WANTED_') and hasattr(self, '_EFFECTS_'):
            for event_path in self._EFFECTS_.keys():
                await self._subscribe_(event_path)
            
            del self.__class__._WANTED_

    async def _subscribe_(self, event_path: str) -> None:
        """
        TODO: Add docstring
        """
        try:
            await self._connection_.subscribe(event_path, cb=self._add_event_)
        except errors.ErrConnectionClosed as exc:
            print(f'(i) Connection closed prematurely: {exc}')
        except errors.ErrTimeout as exc:
            print(
                f'(i) Timeout occured when subscribing [{event_path}]: {exc}'
            )

    async def _add_event_(self, message) -> None:
        """
        TODO: Add docstring
        """
        event_path = message.subject
        event_payload = message.data.decode()

        try:
            event_props = json.loads(event_payload)
        except ValueError:
            # TODO: handle the error
            pass
        else:
            event_props.update({'*event': event_path})

            await self._events_.put(event_props)

    async def _impacting_(self) -> None:
        """
        TODO: Add docstring
        """
        while True:
            event_props = await self._events_.get()

            event_path = event_props.pop('*event', None)
            if event_path in self._EFFECTS_:
                await self._EFFECTS_[event_path](self, **event_props)
