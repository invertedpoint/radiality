"""
radiality:examples:simple:dist:animal:animal.core
"""

from typing import TypeVar
import asyncio

from radiality import Ring

import eventer
import effectors


Self = TypeVar('Self', bound='Animal')


class Animal(eventer.Animal, effectors.Human):
    """TODO: Add docstring"""
    _name: str

    def __init__(self, name: str) -> None:
        """TODO: Add docstring"""
        super().__init__()

        self._name = name

    def attract(self, ring: Ring) -> Self:
        """TODO: Add docstring"""
        ring.focus(self)

        return self

    def arise(self) -> None:
        """TODO: Add docstring"""
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

    def _intro(self) -> None:
        """TODO: Add docstring"""
        print('The `{0}` core running...'.format(self.__class__.__name__))
        channel_uri = self.channel_uri()
        if channel_uri:
            print('and it is available at [{0}]...'.format(channel_uri))

    def _outro(self) -> None:
        """TODO: Add docstring"""
        print('\nThe `{0}` core is stopped'.format(self.__class__.__name__))


class Dog(Animal):
    """TODO: Add docstring"""
    SOUND = 'Woof!'
