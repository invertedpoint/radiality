"""
radiality:radiality.linear.effect

The `radiality/linear/effect.py` is a part of `radiality`.
Apache 2.0 licensed.
"""


def sync_effect(method):
    """
    method: Callable[..., None]

    return: Callable[..., None]

    Decorator for the definition of an `effect`.
    """
    setattr(method, 'IS_EFFECT', True)
    return method
