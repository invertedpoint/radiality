"""
radiality:examples:simple:dist:family:main
"""

import asyncio

from radiality import Ring

from human import core


class Couple:
    _tom = None  # type: human.core.Man
    _mary = None  # type: human.core.Woman

    _task = None  # type: asyncio.Task

    def attract(self, ring):
        """
        self: main.Couple
        ring: radiality.Ring
        """
        self._tom = ring.focus(
            core.Man(name='Tom').sensor('0.0.0.0', 50001)
        )
        self._mary = ring.focus(
            core.Woman(name='Mary').sensor('0.0.0.0', 50002)
        )

        return self

    def arise(self):
        """
        self: main.Couple
        """
        loop = asyncio.get_event_loop()

        try:
            self._task = asyncio.ensure_future(
                asyncio.wait(asyncio.Task.all_tasks())
            )
            loop.call_later(3, self._stop)

            self._tom.arise()
            self._mary.arise()

            loop.run_until_complete(self._task)
        except KeyboardInterrupt:
            pass
        finally:
            self._tom.vanish()
            self._mary.vanish()

            loop.close()

    def _stop(self):
        """
        self: main.Couple
        """
        for task in asyncio.Task.all_tasks():
            if task != self._task:
                task.cancel()


if __name__ == '__main__':
    Couple().attract(Ring().cohere('0.0.0.0', 50000)).arise()
