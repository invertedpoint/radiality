"""
radiality:examples:simple:human:core
"""

import eventer
import effectors


class Human(eventer.Human, effectors.Family, effectors.Animal):
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

    def intro(self) -> None:
        """
        TODO: Add docstring
        """
        core_id = self.__class__.__name__
        print(f'The {core_id} core running...')

    def outro(self) -> None:
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

    async def _say_hello(self) -> None:
        """
        TODO: Add docstring
        """
        # Causes the `hello_said` event
        await self.hello_said(name=self._name)

    def _pay_attention(self, causer: str) -> None:
        """
        TODO: Add docstring
        """
        print(f'{causer} made a sound! -- {self._name} said.')


class Man(Human):
    """
    TODO: Add docstring
    """
    pass


class Woman(Human):
    """
    TODO: Add docstring
    """
    pass
