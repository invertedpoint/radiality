"""
radiality:examples:simple:dist:animal:animal.core
"""

from animal import eventer
from animal import effectors


class Animal(eventer.Animal, effectors.Human):
    _name = None  # type: str

    def __init__(self, name):
        """
        self: animal.core.Animal
        name: str
        """
        super().__init__()

        self._name = name

    def attract(self, ring):
        """
        self: animal.core.Animal
        ring: radiality.Ring
        """
        ring.focus(self)

        return self

    def arise(self):
        """
        self: animal.core.Animal
        """
        loop = asyncio.get_event_loop()

        try:
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


class Dog(Animal):
    pass
