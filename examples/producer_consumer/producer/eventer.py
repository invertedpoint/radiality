"""
radiality:examples:producer_consumer:producer:eventer
"""

from radiality import event
from radiality import Eventer


DEFC = '\x1b[0;32;40m'
ENDC = '\x1b[0m'


class Producer(Eventer):
    """
    TODO: Add docstring
    """

    @event
    async def producing(self, data: str, n: int) -> None:
        """
        TODO: Add docstring
        """
        print(f'{DEFC}Producing {data}/{n}{ENDC}')

    @event
    async def produced(self, data: str, n: int) -> None:
        """
        TODO: Add docstring
        """
        print(f'{DEFC}Produced {data}/{n}{ENDC}')

    @event
    async def completed(self) -> None:
        """
        TODO: Add docstring
        """
        print(f'{DEFC}Completed{ENDC}')
