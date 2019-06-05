"""
radiality:radiality.event

The `radiality/event.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from typing import Callable
from typing import Any
from functools import wraps
from itertools import zip_longest


def event(method: Callable[..., None]) -> Callable[..., None]:
    """
    Decorator for the definition of an event
    """
    event_id = method.__name__
    # Constructs the template for the `event` properties
    n = method.__code__.co_argcount - 1
    keys = method.__code__.co_varnames[n:0:-1]
    defaults = (method.__defaults__ or ())[::-1]
    event_props_tmpl = list(zip_longest(keys, defaults))[::-1]

    if _is_empty_func(method):
        @wraps(method)
        async def _wrapper(self, *args: Any, **kwargs: Any) -> None:
            """
            TODO: Add docstring
            """
            event_props = {
                key: (value if arg is None else arg)
                for ((key, value), arg) in zip_longest(event_props_tmpl, args)
            }
            event_props.update(kwargs)

            await self._actualize_(event_id, event_props)
    else:
        @wraps(method)
        async def _wrapper(self, *args: Any, **kwargs: Any) -> None:
            """
            TODO: Add docstring
            """
            event_props = {
                key: (value if arg is None else arg)
                for ((key, value), arg) in zip_longest(event_props_tmpl, args)
            }
            event_props.update(kwargs)

            await method(self, *args, **kwargs)
            await self._actualize_(event_id, event_props)

    setattr(_wrapper, '_IS_EVENT_', True)

    return _wrapper


def _is_empty_func(func: Callable[..., None]) -> bool:
    """
    Checks if a function is empty
    """
    def _empty_func() -> None:
        pass

    def _empty_func_with_doc() -> None:
        """
        Empty function with docstring
        """
        pass

    return (
        func.__code__.co_code == _empty_func.__code__.co_code
    ) or (
        func.__code__.co_code == _empty_func_with_doc.__code__.co_code
    )
