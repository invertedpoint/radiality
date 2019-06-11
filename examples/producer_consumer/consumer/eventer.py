"""
radiality:examples:producer_consumer:consumer:eventer
"""

from radiality import event
from radiality import Eventer


class Consumer(Eventer):
    """
    TODO: Add docstring
    """

    @event
    async def consuming(self, data: str) -> None:
        """
        TODO: Add docstring
        """
        print(f'⚡ Consuming {data}...')

    @event
    async def consumed(self, data: str) -> None:
        """
        TODO: Add docstring
        """
        print(f'⚡ Consumed {data}')
        # Notifies the queue that data has been processed
        self._finalize_jobs()

    @event
    async def completed(self) -> None:
        """
        TODO: Add docstring
        """
        print('⚡ Completed')

    def _finalize_jobs(self) -> None:
        """
        Notifies the queue that data has been processed
        """
        raise NotImplementedError
