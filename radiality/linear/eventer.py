"""
radiality:radiality.linear.eventer

The `radiality/linear/eventer.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from functools import wraps

from radiality.linear.effector import sync_effect
from radiality.linear.effector import SyncEffector


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


class Ring(SyncEffector):

    @sync_effect
    def systemized(self, cores):
        """
        self: SyncEventer
        cores: defaultdict[str, List[SyncEventer]]
        """
        for core_id in self.WANTED.keys():
            if core_id in cores:
                for core in cores[core_id]:
                    core.focus(self)


class SyncEventer(Ring):
    CORE_ID = None  # type: str

    _effectors = None  # type: List[SyncEffector]

    def __new__(cls, *args, **kwargs):
        """
        cls: Type[SyncEventer]
        *args: Any
        **kwargs: Any

        return: SyncEventer
        """
        if cls.CORE_ID is None:
            eventer_cls = cls._eventer_type()
            core_ids = [
                base_cls.__name__
                for base_cls in cls.__mro__
                if eventer_cls in base_cls.__bases__
            ]

            if len(core_ids) == 1:
                cls.CORE_ID = core_ids[0]
            else:
                # TODO: handle the error
                pass

        return super().__new__(cls)

    def _eventer_type():
        """
        return: Type
        """
        return SyncEventer

    def __init__(self):
        """
        self: SyncEventer
        """
        super().__init__()

        self._effectors = []

    def focus(self, core):
        """
        self: SyncEventer
        core: SyncEventer

        return: SyncEventer
        """
        effector = core.connect()
        if effector not in self._effectors:
            self._effectors.append(effector)

        return core

    def defocus(self, core):
        """
        self: SyncEventer
        core: SyncEventer

        return: SyncEventer
        """
        effector = core.disconnect()
        if effector in self._effectors:
            self._effectors.remove(effector)

        return core

    def _actualize(self, event_id, event_props):
        """
        self: SyncEventer
        event_id: str
        event_props: Tuple[List[Any], Dict[str, Any]]
        """
        event_path = '{core_id}.{event_id}'.format(
            core_id=self.CORE_ID, event_id=event_id
        )
        event_props = (event_path, *event_props)

        for effector in self._effectors:
            SyncEffector.add_event(effector, event_props)


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
