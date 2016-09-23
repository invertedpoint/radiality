"""
center:core.subsystem
"""

import radiality

from core.eventers import center


class Center(radiality.Subsystem):
    """
    The `center` subsystem
    """
    eventer = center.Eventer
