"""
radiality:examples:simple:dist:family.core
"""

import asyncio

from family import eventer


class Family(eventer.Family):

    def attract(self, ring):
        """
        self: family.core.Family
        ring: radiality.Ring
        """
        ring.focus(self)

        return self

    def gather(self):
        """
        self: family.core.Family
        """
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

    def _intro(self):
        """
        self: family.core.Family
        """
        print('The `{0}` core running...'.format(self.__class__.__name__))
        channel_uri = self.channel_uri()
        if channel_uri:
            print('and it is available at [{0}]...'.format(channel_uri))

    def _outro(self):
        """
        self: family.core.Family
        """
        print('\nThe `{0}` core is stopped'.format(self.__class__.__name__))
