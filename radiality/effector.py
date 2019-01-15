"""
radiality:radiality.effector

The `radiality/effector.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from typing import TypeVar
from typing import Dict
from typing import Type
from typing import Callable
import json
import asyncio

from nats.aio import errors

from radiality.connectable import Connectable


Self = TypeVar('Self', bound='Effector')


class Effector(Connectable):
    """
    TODO: Add docstring
    """
    WANTED: Dict[str, Type]
    EFFECTS: Dict[str, Callable[..., None]]

    _events: asyncio.Queue
    _impactor: asyncio.Task

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        """
        TODO: Add docstring
        """
        if not cls.WANTED:
            effector_types = {Effector}
            cls.WANTED = {
                base_cls.__name__: base_cls
                for base_cls in cls.__mro__
                if (base_cls not in effector_types) and (
                    len(effector_types.intersection(base_cls.__bases__)) > 0
                )
            }

        if not cls.EFFECTS:
            cls.EFFECTS = {
                ref.__qualname__: ref
                for effector_cls in cls.WANTED.values()
                for ref in effector_cls.__dict__.values()
                if getattr(ref, 'IS_EFFECT', False)
            }

        return super().__new__(cls)

    def __init__(self) -> None:
        """
        TODO: Add docstring
        """
        super().__init__()

        if self._events is None:
            self._events = asyncio.Queue()

        if self._impactor is None:
            self._impactor = asyncio.ensure_future(self._impacting())

    async def connected(self) -> None:
        """
        TODO: Add docstring
        """
        if self.WANTED and self.EFFECTS:
            for event_path in self.EFFECTS.keys():
                await self._subscribe(event_path)
            
            self.WANTED = {}

    async def _subscribe(self, event_path: str) -> None:
        """
        TODO: Add docstring
        """
        try:
            await self.connection().subscribe(event_path, cb=self._add_event)
        except errors.ErrConnectionClosed as exc:
            print(f'(i) Connection closed prematurely: {exc}')
        except errors.ErrTimeout as exc:
            print(
                f'(i) Timeout occured when subscribing [{event_path}]: {exc}'
            )

    async def _add_event(self, message) -> None:
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

            await self._events.put(event_payload)

    async def _impacting(self) -> None:
        """
        TODO: Add docstring
        """
        while True:
            event_props = await self._events.get()

            event_path = event_props.pop('*event', None)
            if event_path in self.EFFECTS:
                await self.EFFECTS[event_path](self, **event_props)
