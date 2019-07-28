from rohdeschwarz.instruments.vna.channel import Channel

def is_calibrated(self):
    scpi     = 'SENS{0}:CORR:SST?'.format(self.index)
    response = self._vna.query(scpi).replace("'", '').strip()
    return len(response) != 0
Channel.is_calibrated = property(is_calibrated)
