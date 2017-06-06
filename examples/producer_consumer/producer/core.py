"""
radiality:examples:producer_consumer:producer:core
"""

import asyncio
from random import random

import eventer
import effectors


class Producer(eventer.Producer, effectors.Consumer):
    """
    The Producer
    """
    JOBS_NUMBER = 10
    MAX_SLEEP_TIME = 5  # 5 sec

    _task = None  # type: asyncio.Task

    def launch(self):
        loop = asyncio.get_event_loop()

        try:
            self._task = asyncio.ensure_future(
                self._produce(n=self.JOBS_NUMBER)
            )

            print('The `Producer` core running...')
            channel_uri = self.channel_uri()
            if channel_uri:
                print('and it is available at [{0}]...'.format(channel_uri))

            loop.run_until_complete(self._task)
        except KeyboardInterrupt:
            pass
        finally:
            print('\nThe `Producer` core is stopped')
            loop.close()

    async def _produce(self, n):
        for x in range(1, n + 1):
            data = str(x)
            # Causes the `producing` event
            await self.producing(data, n)
            # Simulates i/o operation using sleep
            await asyncio.sleep(self.MAX_SLEEP_TIME * random())
            # Causes the `produced` event
            await self.produced(data, n)
        # Causes the `completed` event
        await self.completed()
        # Stops all tasks
        self._stop()

    def _stop(self):
        for task in asyncio.Task.all_tasks():
            if task != self._task:
                task.cancel()
