import numpy   as     np
from   pathlib import Path

# rohdeschwarz.instruments.vna
# patches
import s2p_extractor.patch.vna.query_64_bit
import s2p_extractor.patch.vna.query_64_bit_complex

class LeaveKeyDict(dict):
    def __missing__(self, key):
        return '{{{0}}}'.format(key)

class Corrections(object):
    def __init__(self):
        self.directivity = np.array([], dtype=np.complex_)
        self.srcmatch    = np.array([], dtype=np.complex_)
        self.refltrack   = np.array([], dtype=np.complex_)
        self.freq        = np.array([], dtype=np.complex_)

    @classmethod
    def from_vna(cls, vna_obj, channel, port):
        params                = LeaveKeyDict()
        params['ch']          = channel
        params['input_port' ] = port
        params['output_port'] = port
        term_scpi = "SENS{ch}:CORR:CDAT? '{term}',{input_port},{output_port}".format_map(params)
        freq_scpi = "SENS{ch}:CORR:STIM?".format_map(params)

        corrections = cls()
        corrections.directivity = vna_obj.query_64_bit_complex(term_scpi.format(term='DIRECTIVITY'))
        corrections.srcmatch    = vna_obj.query_64_bit_complex(term_scpi.format(term='SRCMATCH'   ))
        corrections.refltrack   = vna_obj.query_64_bit_complex(term_scpi.format(term='REFLTRACK'  ))
        corrections.freq        = vna_obj.query_64_bit(freq_scpi)
        return corrections
