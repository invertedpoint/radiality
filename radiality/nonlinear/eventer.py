"""
radiality:radiality.nonlinear.eventer

The `radiality/nonlinear/eventer.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import json
import asyncio
from functools import wraps
from itertools import zip_longest

from radiality.linear.eventer import is_empty_func
from radiality.linear.eventer import SyncEventer
from radiality.nonlinear.effector import AsyncEffector


def async_event(method):
    """
    method: Callable[..., None]

    return: Callable[..., None]

    Decorator for the definition of an `event`.
    """
    event_id = method.__name__
    # Constructs the template for the `event` properties
    n = method.__code__.co_argcount - 1
    keys = method.__code__.co_varnames[n:0:-1]
    defaults = (method.__defaults__ or ())[::-1]
    event_props_tmpl = list(zip_longest(keys, defaults))[::-1]

    if is_empty_func(method):
        @wraps(method)
        async def _wrapper(self, *args, **kwargs):
            """
            self: radiality.???
            *args: Any
            **kwargs: Any
            """
            event_props = {
                key: (value if arg is None else arg)
                for ((key, value), arg) in zip_longest(event_props_tmpl, args)
            }
            event_props.update(kwargs)

            await self._actualize(event_id, event_props)
    else:
        @wraps(method)
        async def _wrapper(self, *args, **kwargs):
            """
            self: radiality.???
            *args: Any
            **kwargs: Any
            """
            event_props = {
                key: (value if arg is None else arg)
                for ((key, value), arg) in zip_longest(event_props_tmpl, args)
            }
            event_props.update(kwargs)

            await method(self, *args, **kwargs)
            await self._actualize(event_id, event_props)

    setattr(_wrapper, 'IS_EVENT', True)

    return _wrapper


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
            tasks = [
                asyncio.ensure_future(
                    AsyncEffector.add_event(effector, event_props)
                )
                for effector in self._effectors
            ]

            if len(tasks) > 0:
                await asyncio.wait(tasks)
