"""
center:core.subsystem
"""

from radiality import Subsystem

from core import eventer


class Center(Subsystem):
    """
    Center subsystem
    """
    eventer = eventer.Center


impl = Center()
