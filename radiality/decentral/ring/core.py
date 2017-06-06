"""
radiality:radiality.decentral.ring.core

The `radiality/decentral/ring/core.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

import asyncio
from collections import defaultdict

from radiality.decentral.effector import TeleEffector
from radiality.decentral.ring import eventer
from radiality.decentral.ring import effectors
from radiality.linear.ring.core import SyncRing


class TeleRing(eventer.TeleRing, effectors.TeleRing):
    """
    Dispatcher of cores
    """
    _base = None  # type: SyncRing

    _channels_uris = None  # type: defaultdict[str, List[str]]

    def __init__(self):
        """
        self: TeleRing
        """
        super().__init__()

        self._base = SyncRing()

        self._channels_uris = defaultdict(list)

    def cohere(self, host, port):
        """
        self: TeleRing
        host: str
        port: int
        """
        if isinstance(host, str) and isinstance(port, int):
            channel_uri = 'ws://{host}:{port}'.format(host=host, port=port)
            asyncio.get_event_loop().run_until_complete(
                self._focus_channel(channel_uri)
            )

        return self

    def launch(self):
        loop = asyncio.get_event_loop()

        try:
            print('The `Ring` core running...')
            channel_uri = self.channel_uri()
            if channel_uri:
                print('and it is available at [{0}]...'.format(channel_uri))

            loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            print('\nThe `Ring` core is stopped')
            loop.close()

    def focus(self, core):
        """
        self: TeleRing
        core: TeleEventer

        return: TeleEventer

        Overridden from `TeleEventer`.
        """
        self._base.focus(core)

        channel_uri = core.channel_uri()
        if channel_uri:
            cores_ids = [
                wanted_core_id
                for (wanted_core_id, effector_cls) in core.WANTED.items()
                if issubclass(effector_cls, TeleEffector)
            ]
            # Causes the `focusing` event
            asyncio.get_event_loop().run_until_complete(
                self.focusing(cores_ids, channel_uri)
            )

        return core
