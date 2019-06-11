"""
radiality:examples:producer_consumer:_pattern:client
"""

import asyncio
import websockets


async def produce(websocket, x, n):
    print('Producing {0}/{1}'.format(x, n))
    await asyncio.sleep(5)
    await websocket.send(str(x))


async def hello(n):
    websocket = await websockets.connect('ws://localhost:8765', max_queue=5)

    tasks = []

    for x in range(1, n + 1):
        task = asyncio.ensure_future(produce(websocket, x, n))
        tasks.append(task)

    await asyncio.gather(*tasks)
    await websocket.send('')
    await websocket.recv()

    await websocket.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(hello(n=1000))
