"""
radiality:radiality.sensority

The `radiality/sensority.py` is a part of `radiality`.
Apache 2.0 licensed.
"""


def effect(method):
    """
    method: Callable[..., None]

    return: Callable[..., None]

    Decorator for the definition of an `effect`.
    """
    setattr(method, 'IS_EFFECT', True)
    return method


class Effector:
    WANTED = None  # type: Dict[str, Type[radiality.sensority.Effector]]
    EFFECTS = None  # type: Dict[str, Callable[..., None]]

    def __new__(cls, *args, **kwargs):
        """
        cls: Type[radiality.sensority.Effector]
        *args: Any
        **kwargs: Any

        return: radiality.sensority.Effector
        """
        if cls.WANTED is None:
            cls.WANTED = {
                base_cls.__name__: base_cls
                for base_cls in cls.__mro__ if Effector in base_cls.__bases__
            }

        if cls.EFFECTS is None:
            cls.EFFECTS = {
                ref.__qualname__: ref
                for effector_cls in cls.WANTED.values()
                for ref in effector_cls.__dict__.values()
                if getattr(ref, 'IS_EFFECT', False)
            }

        return super().__new__(cls)

    def react(self, event_path, *args, **kwargs):
        """
        self: radiality.sensority.Effector
        event_path: str
        *args: Any
        **kwargs: Any
        """
        if event_path in self.EFFECTS:
            self.EFFECTS[event_path](self, *args, **kwargs)
