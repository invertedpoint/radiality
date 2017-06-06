"""
radiality:examples:simple:sync_mono:main
"""

from radiality import Ring

from family import FamilyCore


if __name__ == '__main__':
    FamilyCore().attract(Ring()).gather()
