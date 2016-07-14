"""
storage:core.subsystem
"""

import os

from radiality import Subsystem

from core import eventer
from core import effectors


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')


class Storage(Subsystem):
    """
    Storage subsystem
    """
    configs_dir = CONFIGS_DIR
    url_protocol = 'http'

    eventer = eventer.Storage
    components = (effectors.Center, effectors.Console)


impl = Storage()
