"""
radiality:examples:producer_consumer:producer:eventer
"""

from radiality import event
from radiality import Eventer


class Producer(Eventer):
    """
    TODO: Add docstring
    """

    @event
    async def producing(self, data: str, n: int) -> None:
        """
        TODO: Add docstring
        """
        print(f'⚡ Producing {data}/{n}')

    @event
    async def produced(self, data: str, n: int) -> None:
        """
        TODO: Add docstring
        """
        print(f'⚡ Produced {data}/{n}')

    @event
    async def completed(self) -> None:
        """
        TODO: Add docstring
        """
        print('⚡ Completed')
