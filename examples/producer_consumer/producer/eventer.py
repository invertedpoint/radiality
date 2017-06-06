"""
radiality:examples:producer_consumer:producer:eventer
"""

from radiality import event
from radiality import Eventer


DEFC = '\x1b[0;32;40m'
ENDC = '\x1b[0m'


class Producer(Eventer):

    @event
    async def producing(self, data, n):
        print('{0}Producing {1}/{2}{3}'.format(DEFC, data, n, ENDC))

    @event
    async def produced(self, data, n):
        print('{0}Produced {1}/{2}{3}'.format(DEFC, data, n, ENDC))

    @event
    async def completed(self):
        print('{0}Completed{1}'.format(DEFC, ENDC))
