"""
radiality:examples:simple:dist:animal:animal.core
"""

import asyncio

from animal import eventer
from animal import effectors


class Animal(eventer.Animal, effectors.Human):
    _name = None  # type: str

    def __init__(self, name):
        """
        self: animal.core.Animal
        name: str
        """
        super().__init__()

        self._name = name

    def attract(self, ring):
        """
        self: animal.core.Animal
        ring: radiality.Ring
        """
        ring.focus(self)

        return self

    def arise(self):
        """
        self: animal.core.Animal
        """
        loop = asyncio.get_event_loop()

        try:
            self._intro()
            # Runs the infinite event loop only
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self._outro()
            # Exit
            loop.close()

    def _intro(self):
        """
        self: family.core.Family
        """
        print('The `{0}` core running...'.format(self.__class__.__name__))
        channel_uri = self.channel_uri()
        if channel_uri:
            print('and it is available at [{0}]...'.format(channel_uri))

    def _outro(self):
        """
        self: family.core.Family
        """
        print('\nThe `{0}` core is stopped'.format(self.__class__.__name__))


class Dog(Animal):
    SOUND = 'Woof!'
