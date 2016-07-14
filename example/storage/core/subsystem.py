"""
storage:core.subsystem
"""

from radiality import Subsystem

from core import eventer
from core import effectors


class Storage(Subsystem):
    """
    Storage subsystem
    """
    eventer = eventer.Storage
    components = (effectors.Center, effectors.Console)


impl = Storage()
