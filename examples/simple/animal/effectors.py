"""
radiality:examples:simple:animal:effectors
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

    async def _come_up(self) -> None:
        """
        TODO: Add docstring
        """
        raise NotImplementedError


class Human(Effector):
    """
    TODO: Add docstring
    """

    @effect
    async def hello_said(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        await self._make_sound(causer=name)

    async def _make_sound(self, causer: str) -> None:
        """
        TODO: Add docstring
        """
        raise NotImplementedError
