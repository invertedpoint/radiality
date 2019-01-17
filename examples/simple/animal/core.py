"""
radiality:examples:simple:animal:core
"""

import asyncio

import eventer
import effectors


class Animal(eventer.Animal, effectors.Human):
    """
    TODO: Add docstring
    """
    _name: str

    def __init__(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        super().__init__()

        self._name = name

    def arise(self) -> None:
        """
        TODO: Add docstring
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

    def _intro(self) -> None:
        """
        TODO: Add docstring
        """
        core_id = self.__class__.__name__
        print(f'The {core_id} core running...')

    def _outro(self) -> None:
        """
        TODO: Add docstring
        """
        core_id = self.__class__.__name__
        print(f'\nThe {core_id} core is stopped')


class Dog(Animal):
    """
    TODO: Add docstring
    """
    SOUND = 'Woof!'
