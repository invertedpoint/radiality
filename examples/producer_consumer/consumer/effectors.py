"""
radiality:examples:producer_consumer:consumer:effectors
"""

from typing import Optional

from radiality import effect
from radiality import Effector


class Producer(Effector):
    """
    TODO: Add docstring
    """

    @effect
    async def producing(self, data: str, n: int) -> None:
        """
        TODO: Add docstring
        """
        print('Producing {0}/{1}...'.format(data, n))

    @effect
    async def produced(self, data: str, n: int) -> None:
        """
        TODO: Add docstring
        """
        print('Produced {0}/{1}'.format(data, n))
        await self._add_job(data)

    @effect
    async def completed(self) -> None:
        """
        TODO: Add docstring
        """
        print('Completed')
        await self._add_job(data=None)

    async def _add_job(self, data: Optional[str]) -> None:
        """
        TODO: Add docstring
        """
        raise NotImplementedError
