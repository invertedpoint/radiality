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

    def arise(self):
        """
        self: human.core.Human
        """
        print('The `{0}` core running...'.format(self.CORE_ID))
        channel_uri = self.channel_uri()
        if channel_uri:
            print('and it is available at [{0}]...'.format(channel_uri))

    def vanish(self):
        """
        self: human.core.Human
        """
        print('\nThe `{0}` core is stopped'.format(self.CORE_ID))


class Man(Human):
    pass


class Woman(Human):
    pass
