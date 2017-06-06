"""
radiality:examples:producer_consumer:consumer:effectors
"""

from radiality import effect
from radiality import Effector


class Producer(Effector):

    @effect
    async def producing(self, data, n):
        print('Producing {0}/{1}...'.format(data, n))

    @effect
    async def produced(self, data, n):
        print('Produced {0}/{1}'.format(data, n))
        await self._jobs.put(data)

    @effect
    async def completed(self):
        print('Completed')
        await self._jobs.put(None)
