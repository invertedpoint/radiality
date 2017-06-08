"""
radiality:examples:simple:dist:family:main
"""

from radiality import Ring

from family import core


if __name__ == '__main__':
    Ring().sensor('0.0.0.0', 50000)

    core.Family().sensor('0.0.0.0', 50001).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).gather()
