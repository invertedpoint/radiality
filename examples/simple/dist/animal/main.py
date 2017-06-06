"""
radiality:examples:simple:dist:animal:main
"""

from radiality import Ring

from animal import core


if __name__ == '__main__':
    core.Dog(name='Buddy').sensor('0.0.0.0', 50003).attract(
        Ring().cohere('0.0.0.0', 50000)
    ).arise()
