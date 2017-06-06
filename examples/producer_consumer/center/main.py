"""
radiality:examples:producer_consumer:center:main
"""

from radiality import Ring


if __name__ == '__main__':
    Ring().sensor('0.0.0.0', 50000).launch()
