"""
radiality:examples:simple:dist:family:main
"""

import asyncio

from radiality import Ring

from human import core


class Couple:
    _tom = None  # type: human.core.Man
    _mary = None  # type: human.core.Woman

    def attract(self, ring):
        """
        self: main.Couple
        ring: radiality.Ring
        """
        self._tom = ring.focus(
            core.Man(name='Tom').sensor('0.0.0.0', 50002)
        )
        self._mary = ring.focus(
            core.Woman(name='Mary').sensor('0.0.0.0', 50003)
        )

        return self

    def arise(self):
        """
        self: main.Couple
        """
        loop = asyncio.get_event_loop()

        try:
            self._tom.intro()
            self._mary.intro()
            # Runs the infinite event loop
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self._tom.outro()
            self._mary.outro()
            # Exit
            loop.close()


if __name__ == '__main__':
    Couple().attract(Ring().cohere('0.0.0.0', 50000)).arise()
