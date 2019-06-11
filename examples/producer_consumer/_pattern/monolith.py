"""
radiality:examples:producer_consumer:_pattern:monolith
"""

import asyncio
import random
import time


TASKS_NUMBER = 10
MAX_SLEEP_TIME = 5  # 5 sec


async def produce(queue, n):
    for x in range(1, n + 1):
        # produce an item
        print('Producing {0}/{1}'.format(x, n))
        # simulate i/o operation using sleep
        await asyncio.sleep(MAX_SLEEP_TIME * random.random())
        item = str(x)
        # put the item in the queue
        await queue.put(item)


async def consume(queue, name):
    while True:
        # wait for an item from the producer
        item = await queue.get()

        # process the item
        print('Consuming {0} in {1}...'.format(item, name))
        # simulate i/o operation using sleep
        await asyncio.sleep(MAX_SLEEP_TIME * random.random())

        # Notify the queue that the item has been processed
        queue.task_done()


async def run(n):
    queue = asyncio.Queue()
    # schedule the consumer
    consumer_a = asyncio.ensure_future(consume(queue, 'A'))
    consumer_b = asyncio.ensure_future(consume(queue, 'B'))
    # run the producer and wait for completion
    await produce(queue, n)
    # wait until the consumer has processed all items
    await queue.join()
    # the consumer is still awaiting for an item, cancel it
    consumer_a.cancel()
    consumer_b.cancel()


if __name__ == '__main__':
    t = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(TASKS_NUMBER))
    loop.close()

    elapsed = time.time() - t
    print('Elapsed: {0}'.format(elapsed))
