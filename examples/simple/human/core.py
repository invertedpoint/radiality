"""
radiality:examples:simple:dist:human:core
"""

import eventer
import effectors


class Human(eventer.Human, effectors.Family, effectors.Animal):
    """
    TODO: Add docstring
    """
    _name: str

    def __init__(self, name: str) -> None:
        """TODO: Add docstring"""
        super().__init__()

        self._name = name

    def intro(self) -> None:
        """TODO: Add docstring"""
        print('The `{0}` core running...'.format(self.__class__.__name__))
        channel_uri = self.channel_uri()
        if channel_uri:
            print('and it is available at [{0}]...'.format(channel_uri))

    def outro(self) -> None:
        """TODO: Add docstring"""
        print('\nThe `{0}` core is stopped'.format(self.__class__.__name__))


class Man(Human):
    """TODO: Add docstring"""
    pass


class Woman(Human):
    """TODO: Add docstring"""
    pass
