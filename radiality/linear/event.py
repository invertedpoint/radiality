"""
radiality:radiality.linear.event

The `radiality/linear/event.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from functools import wraps


def sync_event(method):
    """
    method: Callable[..., None]

    return: Callable[..., None]

    Decorator for the definition of an `event`.
    """
    event_id = method.__name__

    if is_empty_func(method):
        @wraps(method)
        def _wrapper(self, *args, **kwargs):
            """
            self: SyncEventer
            *args: Any
            **kwargs: Any
            """
            self._actualize(event_id, event_props=(args, kwargs))
    else:
        @wraps(method)
        def _wrapper(self, *args, **kwargs):
            """
            self: SyncEventer
            *args: Any
            **kwargs: Any
            """
            method(self, *args, **kwargs)
            self._actualize(event_id, event_props=(args, kwargs))

    setattr(_wrapper, 'IS_EVENT', True)

    return _wrapper


def is_empty_func(func):
    """
    func: Callable[..., Any]

    return: bool

    Checks if a function is empty.
    """
    def _empty_func():
        pass

    def _empty_func_with_doc():
        """
        Empty function with docstring
        """
        pass

    return (
        func.__code__.co_code == _empty_func.__code__.co_code
    ) or (
        func.__code__.co_code == _empty_func_with_doc.__code__.co_code
    )


# TODO: Implement the `sync_event` decorator as a class
class SyncEvent:
    _method = None
    _event_path = None

    def __init__(self, method):
        self._method = method

    def __call__(self, core_, *args, **kwargs):
        self._method(core_, *args, **kwargs)
        core_.actualize(
            event_path=self._event_path, event_props=(args, kwargs)
        )

    def setup(self, core_id):
        if self._event_path is None:
            self._event_path = '{core_id}.{event_id}'.format(
                core_id=core_id, event_id=self._method.__name__
            )
