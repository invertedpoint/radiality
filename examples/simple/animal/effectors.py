"""
radiality:examples:simple:dist:animal:animal.effectors
"""

from radiality import effect
from radiality import Effector


class Human(Effector):
    """TODO: Add docstring"""

    @effect
    async def hello_said(self) -> None:
        """TODO: Add docstring"""
        print(self.SOUND)
        # Causes the `sound_made` event
        await self.sound_made(name=self._name)
