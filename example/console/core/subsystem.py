"""
console:core.subsystem
"""

import asyncio
import websockets

from radiality import Effector
from radiality import utils

from core.eventer import Console
from core.effectors import Center
from core.effectors import Storage


CENTER_SID = 'center'
CENTER_HOST = 'center'
CENTER_PORT = 8888
CENTER_FREQ = utils.subsystem_freq(CENTER_HOST, CENTER_PORT)


eventer = Console()
effectors = {
    'center': Center,
    'storage': Storage
}


@asyncio.coroutine
def receiver(channel, path):
    effector = effectors.get(path[1:], Effector)(eventer, channel)

    receiving = True
    while receiving:
        receiving = yield from effector.activate()


@asyncio.coroutine
def launcher():
    yield from eventer.connect(sid=CENTER_SID, freq=CENTER_FREQ)
    yield from eventer.connected(sid=CENTER_SID)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()

    try:
        serving = websockets.serve(receiver, eventer.host, eventer.port)
        event_loop.run_until_complete(serving)
        print('[i] Serving on {0}'.format(eventer.freq))

        event_loop.run_until_complete(launcher())

        event_loop.run_forever()
    finally:
        event_loop.close()
