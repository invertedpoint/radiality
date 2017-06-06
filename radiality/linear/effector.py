"""
radiality:radiality.linear.effector

The `radiality/linear/effector.py` is a part of `radiality`.
Apache 2.0 licensed.
"""


class SyncEffector:
    WANTED = None  # type: Dict[str, Type]
    EFFECTS = None  # type: Dict[str, Callable[..., None]]

    def __new__(cls, *args, **kwargs):
        """
        cls: Type[SyncEffector]
        *args: Any
        **kwargs: Any

        return: SyncEffector
        """
        if cls.WANTED is None:
            effector_types = cls._effector_types()
            cls.WANTED = {
                base_cls.__name__: base_cls
                for base_cls in cls.__mro__
                if (base_cls not in effector_types) and (
                    len(effector_types.intersection(base_cls.__bases__)) > 0
                )
            }

        if cls.EFFECTS is None:
            cls.EFFECTS = {
                ref.__qualname__: ref
                for effector_cls in cls.WANTED.values()
                for ref in effector_cls.__dict__.values()
                if getattr(ref, 'IS_EFFECT', False)
            }

        return super().__new__(cls)

    def _effector_types():
        """
        return: Set[Type]
        """
        return {SyncEffector}

    def connect(self):
        """
        self: SyncEffector

        return: SyncEffector
        """
        return self

    def disconnect(self):
        """
        self: SyncEffector

        return: SyncEffector
        """
        return self

    def add_event(self, event_props):
        """
        self: SyncEffector
        event_props: Tuple[str, List[Any], Dict[str, Any]]
        """
        (event_path, args, kwargs) = event_props

        if event_path in self.EFFECTS:
            self.EFFECTS[event_path](self, *args, **kwargs)
