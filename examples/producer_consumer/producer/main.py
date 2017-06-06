"""
radiality:examples:producer_consumer:producer:main
"""

from radiality import Ring

from core import Producer


if __name__ == '__main__':
    Ring().cohere('0.0.0.0', 50000).focus(
        Producer().sensor('0.0.0.0', 50001)
    ).launch()
