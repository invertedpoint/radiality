"""
radiality:examples:simple:human:main
"""

from typing import TypeVar
import asyncio

import core


Self = TypeVar('Self', bound='Couple')


class Couple:
    """
    TODO: Add docstring
    """
    _tom: core.Man
    _mary: core.Woman

    def cohere(self, scheme: str, host: str, port: int) -> Self:
        """
        TODO: Add docstring
        """
        self._tom = core.Man(name='Tom').cohere(scheme, host, port)
        self._mary = core.Woman(name='Mary').cohere(scheme, host, port)

        return self

    def arise(self):
        """
        TODO: Add docstring
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
    Couple().cohere('nats', '127.0.0.1', 4222).arise()
