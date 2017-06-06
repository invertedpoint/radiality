"""
radiality:examples:simple:dist:family:main
"""

from radiality import Ring

from family import core


if __name__ == '__main__':
    core.Family().attract(Ring().sensor('0.0.0.0', 50000)).gather()
