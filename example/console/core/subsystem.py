"""
console:core.subsystem
"""

import os

from radiality import Subsystem

from core import eventer
from core import effectors
from core import actions


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')


class Console(Subsystem):
    """
    Console subsystem
    """
    configs_dir = CONFIGS_DIR
    url_protocol = 'http'

    eventer = eventer.Console
    components = (effectors.Center, effectors.Storage, actions.Sample)


impl = Console()
