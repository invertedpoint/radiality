"""
radiality:examples:producer_consumer:consumer:main
"""

from radiality import Ring

from core import Consumer


if __name__ == '__main__':
    Ring().cohere('0.0.0.0', 50000).focus(
        Consumer().sensor('0.0.0.0', 50002)
    ).launch()
