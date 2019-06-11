"""
radiality:examples:simple:human:effectors
"""

from radiality import effect
from radiality import Effector


class Family(Effector):
    """
    TODO: Add docstring
    """

    @effect
    async def gathering(self) -> None:
        """
        TODO: Add docstring
        """
        await self._come_up()

    @effect
    async def gathered(self) -> None:
        """
        TODO: Add docstring
        """
        await self._say_hello()

    async def _come_up(self) -> None:
        """
        TODO: Add docstring
        """
        raise NotImplementedError

    async def _say_hello(self) -> None:
        """
        TODO: Add docstring
        """
        raise NotImplementedError


class Animal(Effector):
    """
    TODO: Add docstring
    """

    @effect
    async def sound_made(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        self._pay_attention(causer=name)

    def _pay_attention(self, causer: str) -> None:
        """
        TODO: Add docstring
        """
        raise NotImplementedError
