"""
radiality:radiality.mutability

The `radiality/mutability.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from functools import wraps

from radiality.sensority import effect
from radiality.sensority import Effector


def event(method):
    """
    method: Callable[..., None]

    return: Callable[..., None]

    Decorator for the definition of an `event`.
    """
    event_id = method.__name__

    @wraps(method)
    def _wrapper(self, *args, **kwargs):
        """
        self: radiality.mutability.Eventer
        *args: Any
        **kwargs: Any
        """
        method(self, *args, **kwargs)
        self.actualize(event_id, *args, **kwargs)

    setattr(_wrapper, 'IS_EVENT', True)

    return _wrapper


class Ringing(Effector):

    @effect
    def systemized(self, cores):
        """
        self: radiality.mutability.Eventer
        cores: defaultdict[str, List[radiality.mutability.Eventer]]
        """
        for core_id in self.WANTED.keys():
            if core_id in cores:
                for core in cores[core_id]:
                    core.focus(self)


class Eventer(Ringing):
    CORE_ID = None  # type: str

    _effectors = None  # type: List[radiality.mutability.Eventer]

    def __new__(cls, *args, **kwargs):
        """
        cls: Type[radiality.mutability.Eventer]
        *args: Any
        **kwargs: Any

        return: radiality.mutability.Eventer
        """
        if cls.CORE_ID is None:
            core_ids = [
                base_cls.__name__
                for base_cls in cls.__mro__ if Eventer in base_cls.__bases__
            ]

            if len(core_ids) == 1:
                cls.CORE_ID = core_ids[0]
            else:
                # TODO: handle the error
                pass

        return super().__new__(cls)

    def __init__(self):
        """
        self: radiality.mutability.Eventer
        """
        self._effectors = []

    def focus(self, core):
        """
        self: radiality.mutability.Eventer
        core: radiality.mutability.Eventer

        return: radiality.mutability.Eventer
        """
        if core not in self._effectors:
            self._effectors.append(core)

        return core

    def defocus(self, core):
        """
        self: radiality.mutability.Eventer
        core: radiality.mutability.Eventer

        return: radiality.mutability.Eventer
        """
        if core in self._effectors:
            self._effectors.remove(core)

        return core

    def actualize(self, event_id, *args, **kwargs):
        """
        self: radiality.mutability.Eventer
        event_id: str
        *args: Any
        **kwargs: Any
        """
        event_path = '{core_id}.{event_id}'.format(
            core_id=self.CORE_ID, event_id=event_id
        )

        for effector in self._effectors:
            effector.react(event_path, *args, **kwargs)
