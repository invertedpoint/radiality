"""
radiality:examples:simple:dist:human.core
"""

from human import eventer
from human import effectors


class Human(eventer.Human, effectors.Family, effectors.Animal):
    _name = None  # type: str

    def __init__(self, name):
        """
        self: human.core.Human
        name: str
        """
        super().__init__()

        self._name = name

    def intro(self):
        """
        self: human.core.Human
        """
        print('The `{0}` core running...'.format(self.__class__.__name__))
        channel_uri = self.channel_uri()
        if channel_uri:
            print('and it is available at [{0}]...'.format(channel_uri))

    def outro(self):
        """
        self: human.core.Human
        """
        print('\nThe `{0}` core is stopped'.format(self.__class__.__name__))


class Man(Human):
    pass


class Woman(Human):
    pass
