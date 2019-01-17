"""
radiality:examples:simple:animal:main
"""

import core


if __name__ == '__main__':
    core.Dog(name='Buddy').cohere('nats', '127.0.0.1', 4222).arise()
