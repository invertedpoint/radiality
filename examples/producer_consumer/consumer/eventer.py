"""
radiality:examples:producer_consumer:consumer:eventer
"""

from radiality import event
from radiality import Eventer


DEFC = '\x1b[0;30;47m'
ENDC = '\x1b[0m'


class Consumer(Eventer):

    @event
    async def consuming(self, data):
        print('{0}Consuming {1}...{2}'.format(DEFC, data, ENDC))

    @event
    async def consumed(self, data):
        print('{0}Consumed {1}{2}'.format(DEFC, data, ENDC))
        # Notifies the queue that data has been processed
        self._jobs.task_done()

    @event
    async def completed(self):
        print('{0}Completed{1}'.format(DEFC, ENDC))
