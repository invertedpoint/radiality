"""
radiality:examples:producer_consumer:consumer:core
"""

from typing import Optional
import asyncio
from random import random

import eventer
import effectors


class Consumer(eventer.Consumer, effectors.Producer):
    """
    The Consumer
    """
    MAX_SLEEP_TIME = 5  # 5 sec

    _jobs: asyncio.Queue
    _task: asyncio.Task

    def arise(self) -> None:
        """
        TODO: Add docstring
        """
        loop = asyncio.get_event_loop()

        try:
            self._intro()

            self._jobs = asyncio.Queue()
            self._task = asyncio.ensure_future(self._consume())

            loop.run_until_complete(self._task)
        except KeyboardInterrupt:
            pass
        finally:
            self._outro()
            # Exit
            loop.close()

    def _intro(self) -> None:
        """
        TODO: Add docstring
        """
        core_id = self.__class__.__name__
        print(f'(i) The {core_id} core running...')

    def _outro(self) -> None:
        """
        TODO: Add docstring
        """
        core_id = self.__class__.__name__
        print(f'\n(i) The {core_id} core is stopped')

    async def _consume(self) -> None:
        """
        TODO: Add docstring
        """
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

    def _stop(self) -> None:
        """
        TODO: Add docstring
        """
        for task in asyncio.Task.all_tasks():
            if task != self._task:
                task.cancel()

    async def _add_job(self, data: Optional[str]) -> None:
        """
        TODO: Add docstring
        """
        await self._jobs.put(data)

    def _finalize_jobs(self) -> None:
        """
        Notifies the queue that data has been processed
        """
        self._jobs.task_done()
