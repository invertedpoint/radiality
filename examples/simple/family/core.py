"""
radiality:examples:simple:family:core
"""

import asyncio

import eventer


class Family(eventer.Family):
    """
    TODO: Add docstring
    """

    def gather(self) -> None:
        """
        TODO: Add docstring
        """
        loop = asyncio.get_event_loop()

        try:
            self._intro()
            # Causes the `gathered` event
            loop.run_until_complete(asyncio.sleep(5))
            loop.run_until_complete(self.gathered())
            # Runs the infinite event loop
            loop.run_forever()
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
        print(f'The {core_id} core running...')

    def _outro(self) -> None:
        """
        TODO: Add docstring
        """
        core_id = self.__class__.__name__
        print(f'\nThe {core_id} core is stopped')
