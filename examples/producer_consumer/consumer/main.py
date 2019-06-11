"""
radiality:examples:producer_consumer:consumer:main
"""

from core import Consumer


if __name__ == '__main__':
    Consumer().cohere('nats', '127.0.0.1', 4222).arise()
