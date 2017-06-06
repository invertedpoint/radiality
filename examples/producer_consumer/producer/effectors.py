"""
radiality:examples:producer_consumer:producer:effectors
"""

from radiality import effect
from radiality import Effector


class Consumer(Effector):

    @effect
    async def consuming(self, data):
        print('Consuming {0}...'.format(data))

    @effect
    async def consumed(self, data):
        print('Consumed {0}'.format(data))

    @effect
    async def completed(self):
        print('Completed')
