"""
radiality:examples:simple:dist:family:core
"""

from typing import TypeVar
import asyncio

from radiality import Ring

import eventer


Self = TypeVar('Self', bound='Family')


class Family(eventer.Family):
    """TODO: Add docstring"""

    def attract(self, ring: Ring) -> Self:
        """TODO: Add docstring"""
        ring.focus(self)

        return self

    def gather(self) -> None:
        """TODO: Add docstring"""
        loop = asyncio.get_event_loop()

        try:
            self._intro()
            # Waits more than `radiality.Eventer.RECONN_WAIT_TIME` sec
            # TODO: Explain this ^^^
            loop.run_until_complete(asyncio.sleep(2))
            # Causes the `gathered` event
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
        """TODO: Add docstring"""
        print('The `{0}` core running...'.format(self.__class__.__name__))
        channel_uri = self.channel_uri()
        if channel_uri:
            print('and it is available at [{0}]...'.format(channel_uri))

    def _outro(self) -> None:
        """TODO: Add docstring"""
        print('\nThe `{0}` core is stopped'.format(self.__class__.__name__))
