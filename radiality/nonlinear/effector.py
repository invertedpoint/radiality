"""
radiality:radiality.nonlinear.effector

The `radiality/nonlinear/effector.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import json
import asyncio

from radiality.linear.effector import SyncEffector


class AsyncEffector(SyncEffector):
    _events = None  # type: asyncio.Queue
    _impactor = None  # type: asyncio.Task

    def _effector_types():
        """
        return: Set[Type]

        Overridden from `SyncEffector`.
        """
        return SyncEffector._effector_types().union({AsyncEffector})

    def __init__(self):
        """
        self: AsyncEffector
        """
        super().__init__()

        if self._events is None:
            self._events = asyncio.Queue()
        if self._impactor is None:
            self._impactor = asyncio.ensure_future(self._impacting())

    async def add_event(self, event_props):
        """
        self: AsyncEffector
        event_props: str

        Overridden from `SyncEffector`.
        """
        await self._events.put(event_props)

    async def _impacting(self):
        """
        self: AsyncEffector
        """
        while True:
            try:
                event_props = await self._events.get()
                event_props = json.loads(event_props)
            except ValueError:
                # TODO: handle the error
                pass
            else:
                event_path = event_props.pop('*event', None)
                if event_path in self.EFFECTS:
                    await self.EFFECTS[event_path](self, **event_props)
