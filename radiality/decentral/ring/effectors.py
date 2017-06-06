"""
radiality:radiality.decentral.ring.effectors

The `radiality/decentral/ring/effectors.py` is a part of `radiality`.
Apache 2.0 licensed.
"""

from radiality.nonlinear.effect import async_effect
from radiality.decentral.effector import TeleEffector


class TeleRing(TeleEffector):

    @async_effect
    async def focusing(self, cores_ids, channel_uri):
        """
        self: radiality.decentral.ring.core.TeleRing
        cores_ids: List[str]
        channel_uri: str
        """
        await self._focus_channel(channel_uri)

        for core_id in cores_ids:
            self._channels_uris[core_id].append(channel_uri)
        # Causes the `systemized` event
        await self.systemized(channels_uris=dict(self._channels_uris))
