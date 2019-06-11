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

    _task: asyncio.Task

    def arise(self) -> None:
        """
        TODO: Add docstring
        """
        loop = asyncio.get_event_loop()

        try:
            self._intro()

            self._task = asyncio.ensure_future(
                self._produce(n=self.JOBS_NUMBER)
            )
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

    async def _produce(self, n: int) -> None:
        """
        TODO: Add docstring
        """
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
