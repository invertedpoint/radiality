"""
center:core.subsystem
"""

import asyncio
import websockets

from eventer import Center
from effectors import Subsystem


eventer = Center()


@asyncio.coroutine
def receiver(channel, path):
    print(path)
    effector = Subsystem(eventer, channel)

    receiving = True
    while receiving:
        receiving = yield from effector.activate()


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()

    try:
        serving = websockets.serve(receiver, eventer.host, eventer.port)
        event_loop.run_until_complete(serving)
        print('[i] Serving on {0}'.format(eventer.freq))

        event_loop.run_forever()
    finally:
        event_loop.close()
