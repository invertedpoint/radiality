"""
radiality:examples:simple:animal:core
"""

import asyncio

import eventer
import effectors


class Animal(eventer.Animal, effectors.Family, effectors.Human):
    """
    TODO: Add docstring
    """
    SOUND: str

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

    async def _come_up(self) -> None:
        """
        TODO: Add docstring
        """
        # Causes the `came` event
        await self.came(name=self._name)

    async def _make_sound(self, causer: str) -> None:
        """
        TODO: Add docstring
        """
        print(f'{self.SOUND} for {causer}')
        # Causes the `sound_made` event
        await self.sound_made(name=self._name)


class Dog(Animal):
    """
    TODO: Add docstring
    """
    SOUND = 'Woof!'
