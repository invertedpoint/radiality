"""
radiality:examples:producer_consumer:_pattern:server
"""

import asyncio
import websockets


async def process(websocket, x):
    print('Processing: {0}'.format(x))
    await asyncio.sleep(5)
    print('Completed: {0}'.format(x))


async def hello(websocket, path):
    while True:
        x = await websocket.recv()
        if x == '':
            break

        await process(websocket, x)

    await websocket.send('')


if __name__ == '__main__':
    server = websockets.serve(hello, 'localhost', 8765, max_queue=5)

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
