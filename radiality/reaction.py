"""
radiality:radiality.reaction

The `radiality/reaction.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from functools import wraps
import json

import asyncio
from websockets.exceptions import ConnectionClosed

from radiality import watch
from radiality import circuit


def effect(method):
    """
    Decorator for the definition of an `effect`
    """
    method = asyncio.coroutine(method)
    # Stores the `effect` specification keys
    effect_spec_keys = set(method.__code__.co_varnames)

    @wraps(method)
    def _wrapper(self, event_spec):
        if set(event_spec.keys()) == effect_spec_keys:
            yield from method(self, **event_spec)
        else:
            self._specs_keys_conflict(
                event_spec_keys=set(event_spec.keys()),
                effect_spec_keys=effect_spec_keys
            )

    _wrapper._is_effect = True

    return asyncio.coroutine(_wrapper)


class Effector(watch.Loggable, circuit.Connectable):
    """
    Receiver of the specific events
    """
    _eventer = None  # type: Eventer
    _channel = None  # type: WebSocketServerProtocol

    _effects = None  # type: dict of str -> method

    def __new__(cls, *args, **kwargs):
        """
        Pre-initialization
        """
        cls._effects = {}
        for (name, method) in cls.__dict__.items():
            if getattr(method, '_is_effect', False):
                cls._effects[name] = method

        return super().__new__(cls, *args, **kwargs)

    def __init__(self, logger, connector, eventer, channel):
        """
        Initialization
        """
        self._logger = logger
        self._connector = connector

        self._eventer = eventer
        self._channel = channel

    @property
    def eventer(self):
        return self._eventer

    # overridden from `circuit.Connectable`
    @asyncio.coroutine
    def connect(self, sid, freq):
        channel = yield from super().connect(sid, freq)
        if channel:
            yield from self._connecting(channel)

        return channel

    @asyncio.coroutine
    def activate(self):
        try:
            spec = yield from self._channel.recv()
            spec = json.loads(spec)
        except ConnectionClosed:
            self.warn('Connection closed')
            return False
        except ValueError:
            self.fail(
                'Invalid input -- '
                'could not decode the event specification: %s', str(spec)
            )
        else:
            yield from self._parse(spec)

        return True

    @asyncio.coroutine
    def _connecting(self, channel):
        spec = {'*signal': 'connecting', 'sid': self.sid, 'freq': self.freq}

        try:
            spec = json.dumps(spec)
            yield from channel.send(spec)
        except ValueError:
            self.fail(
                'Invalid output -- '
                'could not encode the signal specification: %s', str(spec)
            )
        except ConnectionClosed:
            self.fail('Connection closed')

    @asyncio.coroutine
    def _parse(self, spec):
        event = spec.pop('*event', None)

        if event in self._effects:
            yield from self._effects[event](self, spec)
        elif event is None:
            self.fail(
                'Invalid input -- '
                'could not decode the event specification: %s', str(spec)
            )
        else:
            self.warn('Unknown event -- {0}'.format(event))

    def _specs_keys_conflict(self, event_spec_keys, effect_spec_keys):
        self.fail(
            'The `event` specification keys did not match the `effect` '
            'specification keys: %s vs. %s',
            str(event_spec_keys), str(effect_spec_keys)
        )
