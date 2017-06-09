"""
radiality:examples:simple:sync_mono:main
"""

from radiality.linear import Ring

from family import FamilyCore


if __name__ == '__main__':
    FamilyCore().attract(Ring()).gather()
