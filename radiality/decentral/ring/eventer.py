"""
radiality:radiality.decentral.ring.eventer

The `radiality/decentral/ring/eventer.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from radiality.nonlinear.event import async_event
from radiality.decentral.eventer import TeleEventer


class TeleRing(TeleEventer):

    @async_event
    async def focusing(self, cores_ids, channel_uri):
        """
        self: radiality.decentral.ring.core.TeleRing
        cores_ids: List[str]
        channel_uri: str
        """
        pass

    @async_event
    async def systemized(self, channels_uris):
        """
        self: radiality.decentral.ring.core.TeleRing
        channels_uris: Dict[str, List[str]]
        """
        pass
