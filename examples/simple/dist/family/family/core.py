"""
radiality:examples:simple:dist:family.core
"""

import asyncio

from family import eventer


class Family(eventer.Family):
    _task = None  # type: asyncio.Task

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
            # Causes the `gathered` event
            loop.run_until_complete(self.gathered())

            self._task = asyncio.ensure_future(
                asyncio.wait(asyncio.Task.all_tasks())
            )
            loop.call_later(3, self._stop)

            print('The `{0}` core running...'.format(self.CORE_ID))
            channel_uri = self.channel_uri()
            if channel_uri:
                print('and it is available at [{0}]...'.format(channel_uri))

            loop.run_until_complete(self._task)
        except KeyboardInterrupt:
            pass
        finally:
            print('\nThe `{0}` core is stopped'.format(self.CORE_ID))
            loop.close()

    def _stop(self):
        """
        self: family.core.Family
        """
        for task in asyncio.Task.all_tasks():
            if task != self._task:
                task.cancel()
