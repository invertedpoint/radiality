"""
radiality:radiality.effect

The `radiality/effect.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from typing import Callable
import asyncio


def effect(method: Callable[..., None]) -> Callable[..., None]:
    """
    Decorator for the definition of an effect
    """
    if asyncio.iscoroutinefunction(method):
        setattr(method, '_IS_EFFECT_', True)

    return method
