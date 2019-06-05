"""
radiality:examples:producer_consumer:producer:effectors
"""

from radiality import effect
from radiality import Effector


class Consumer(Effector):
    """
    TODO: Add docstring
    """

    @effect
    async def consuming(self, data: str) -> None:
        """
        TODO: Add docstring
        """
        print(f'Consuming {data}...')

    @effect
    async def consumed(self, data: str) -> None:
        """
        TODO: Add docstring
        """
        print(f'Consumed {data}')

    @effect
    async def completed(self) -> None:
        """
        TODO: Add docstring
        """
        print('Completed')
