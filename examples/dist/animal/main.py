"""
radiality:examples:dist:animal:main
"""

from radiality import Ring

from animal.core import Family


if __name__ == '__main__':
    Ring(point='127.0.0.1:50000').focus(Family(point='127.0.0.1:50100'))
