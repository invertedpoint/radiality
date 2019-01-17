"""
radiality:examples:simple:family:core
"""

import asyncio

import eventer
import effectors


class Family(eventer.Family, effectors.Human, effectors.Animal):
    """
    TODO: Add docstring
    """
    _expected_members = {'Tom', 'Mary', 'Buddy'}

    def arise(self) -> None:
        """
        TODO: Add docstring
        """
        loop = asyncio.get_event_loop()

        try:
            self._intro()
            # Tries to gather all family members
            loop.run_until_complete(self._gathering())
            # Runs the infinite event loop only
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

    async def _gathering(self) -> None:
        """
        TODO: Add docstring
        """
        while len(self._expected_members) > 0:
            print('(i) Gathering...')
            # Causes the `gathering` event
            await self.gathering()
            # Waits a little before the re-causing of the `gathering` event
            await asyncio.sleep(1)
        # Causes the `gathered` event
        await self.gathered()

    def _stop_expecting(self, name: str) -> None:
        """
        TODO: Add docstring
        """
        if name in self._expected_members:
            print(f'(i) {name} came.')
            self._expected_members.remove(name)
