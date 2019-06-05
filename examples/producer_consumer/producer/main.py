"""
radiality:examples:producer_consumer:producer:main
"""

from core import Producer


if __name__ == '__main__':
    Producer().cohere('nats', '127.0.0.1', 4222).arise()
