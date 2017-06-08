"""
radiality:examples:simple:dist:animal:animal.effectors
"""

from radiality import effect
from radiality import Effector


class Human(Effector):

    @effect
    async def hello_said(self):
        """
        self: animal.core.Animal
        """
        print(self.SOUND)
        # Causes the `sound_made` event
        await self.sound_made(name=self._name)
