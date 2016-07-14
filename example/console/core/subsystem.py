"""
console:core.subsystem
"""

from radiality import Subsystem

from core import eventer
from core import effectors
from core import actions


class Console(Subsystem):
    """
    Console subsystem
    """
    eventer = eventer.Console
    components = (effectors.Center, effectors.Storage, actions.Sample)


impl = Console()
