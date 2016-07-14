"""
center:core.subsystem
"""

import os

from radiality import Subsystem

from core import eventer


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGS_DIR = os.path.join(BASE_DIR, 'configs')


class Center(Subsystem):
    """
    Center subsystem
    """
    configs_dir = CONFIGS_DIR
    url_protocol = 'http'

    eventer = eventer.Center


impl = Center()
