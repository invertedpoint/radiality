"""
radiality:radiality.nonlinear.eventer

The `radiality/nonlinear/eventer.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import json
import asyncio

from radiality.linear.eventer import SyncEventer
from radiality.nonlinear.effector import AsyncEffector


class AsyncEventer(SyncEventer):

    def _eventer_type():
        """
        return: Type

        Overridden from `SyncEventer`.
        """
        return AsyncEventer

    async def _actualize(self, event_id, event_props):
        """
        self: AsyncEventer
        event_id: str
        event_props: Dict[str, Any]

        Overridden from `SyncEventer`.
        """
        event_path = '{core_id}.{event_id}'.format(
            core_id=self.CORE_ID, event_id=event_id
        )
        event_props.update({'*event': event_path})

        try:
            event_props = json.dumps(event_props)
        except ValueError:
            # TODO: handle the error
            pass
        else:
            tasks = self._actualization_tasks(event_props)
            if len(tasks) > 0:
                await asyncio.wait(tasks)

    def _actualization_tasks(self, event_props):
        """
        self: AsyncEventer
        event_props: Dict[str, Any]

        return: List[asyncio.Task]
        """
        return [
            asyncio.ensure_future(
                AsyncEffector.add_event(effector, event_props)
            )
            for effector in self._effectors
        ]
