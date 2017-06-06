"""
radiality:examples:producer_consumer:consumer:core
"""

import asyncio
from random import random

import eventer
import effectors


class Consumer(eventer.Consumer, effectors.Producer):
    """
    The Consumer
    """
    MAX_SLEEP_TIME = 5  # 5 sec

    _jobs = None  # type: asyncio.Queue
    _task = None  # type: asyncio.Task

    def launch(self):
        loop = asyncio.get_event_loop()

        try:
            self._jobs = asyncio.Queue()
            self._task = asyncio.ensure_future(self._consume())

            print('The `Consumer` core running...')
            channel_uri = self.channel_uri()
            if channel_uri:
                print('and it is available at [{0}]...'.format(channel_uri))

            loop.run_until_complete(self._task)
        except KeyboardInterrupt:
            pass
        finally:
            print('\nThe `Consumer` core is stopped')
            loop.close()

    async def _consume(self):
        while True:
            data = await self._jobs.get()
            if data is None:  # => producing is completed
                break
            # Causes the `consuming` event
            await self.consuming(data)
            # Simulates i/o operation using sleep
            await asyncio.sleep(self.MAX_SLEEP_TIME * random())
            # Causes the `consumed` event
            await self.consumed(data)
        # Causes the `completed` event
        await self.completed()
        # Stops all tasks
        self._stop()

    def _stop(self):
        for task in asyncio.Task.all_tasks():
            if task != self._task:
                task.cancel()
