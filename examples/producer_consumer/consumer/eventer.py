"""
radiality:examples:producer_consumer:consumer:eventer
"""

from radiality import event
from radiality import Eventer


DEFC = '\x1b[0;30;47m'
ENDC = '\x1b[0m'


class Consumer(Eventer):
    """
    TODO: Add docstring
    """

    @event
    async def consuming(self, data: str) -> None:
        """
        TODO: Add docstring
        """
        print(f'{DEFC}Consuming {data}...{ENDC}')

    @event
    async def consumed(self, data: str) -> None:
        """
        TODO: Add docstring
        """
        print(f'{DEFC}Consumed {data}{ENDC}')
        # Notifies the queue that data has been processed
        self._finalize_jobs()

    @event
    async def completed(self) -> None:
        """
        TODO: Add docstring
        """
        print(f'{DEFC}Completed{ENDC}')

    def _finalize_jobs(self) -> None:
        """
        Notifies the queue that data has been processed
        """
        raise NotImplementedError
