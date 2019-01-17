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
        # Causes the `came` event
        await self.came(name=self._name)


class Human(Effector):
    """
    TODO: Add docstring
    """

    @effect
    async def hello_said(self, name) -> None:
        """
        TODO: Add docstring
        """
        print(f'{self.SOUND} for {name}')
        # Causes the `sound_made` event
        await self.sound_made(name=self._name)
