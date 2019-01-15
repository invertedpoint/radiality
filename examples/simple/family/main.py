"""
radiality:examples:simple:dist:family:main
"""

from radiality import Ring

import core


if __name__ == '__main__':
    Ring('nats://127.0.0.1:4222').sensor('0.0.0.0', 50000)

    core.Family().sensor('0.0.0.0', 50001).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).gather()
