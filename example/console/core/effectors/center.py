"""
console:core.effectors.center
"""

import radiality


class Effector(radiality.Effector):
    """
    Effector for the handling of events of the `center` subsystem
    """

    @radiality.effect
    def systemized(self, signal):
        self.log('subsystems')
        subsystems = signal.get('subsystems', [])

        for (sid, freq) in subsystems:
            if sid in self.wanted:
                yield from self.connect(sid, freq)

                if sid == 'storage':
                    yield from self.eventer.ping()
