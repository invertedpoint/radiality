"""
radiality:radiality.nonlinear.effect

The `radiality/nonlinear/effect.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import asyncio


def async_effect(method):
    """
    method: Callable[..., None]

    return: Callable[..., None]

    Decorator for the definition of an `effect`.
    """
    if asyncio.iscoroutinefunction(method):
        setattr(method, 'IS_EFFECT', True)

    return method
