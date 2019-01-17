"""
radiality:examples:simple:family:main
"""

import core


if __name__ == '__main__':
    core.Family().cohere('nats', '127.0.0.1', 4222).arise()
