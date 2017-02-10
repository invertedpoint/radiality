"""
radiality:example:dist:family:main
"""

from radiality import Ring

from core import Family


if __name__ == '__main__':
    Ring(point='127.0.0.1:50000').focus(Family(point='127.0.0.1:50100'))
