"""
radiality:examples:simple:animal:effectors
"""

from radiality import effect
from radiality import Effector


class Human(Effector):
    """
    TODO: Add docstring
    """

    @effect
    async def came(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        self._stop_expecting(name)


class Animal(Effector):
    """
    TODO: Add docstring
    """

    @effect
    async def came(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        self._stop_expecting(name)
