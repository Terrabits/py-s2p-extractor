import numpy as np
import s2p_extractor.patch.vna.channel_is_calibrated
import s2p_extractor.patch.vna.query_64_bit
import s2p_extractor.patch.vna.query_64_bit_complex

class TempChannel(object):
    def __init__(self, vna_obj, index=None):
        self.vna = vna_obj
        if index:
            self.index = index
        else:
            self.index = vna_obj.create_channel()
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.vna.delete_channel(self.index)

class Corrections(object):
    def __init__(self):
        self.directivity = np.array([], dtype=np.complex_)
        self.srcmatch    = np.array([], dtype=np.complex_)
        self.refltrack   = np.array([], dtype=np.complex_)
        self.freq        = np.array([], dtype=np.complex_)

    @property
    def is_empty(self):
        if self.directivity.size == 0:
            return True
        if self.srcmatch.size    == 0:
            return True
        if self.refltrack.size   == 0:
            return True
        if self.freq.size        == 0:
            return True
        # else
        return False

    @property
    def is_valid(self):
        SIZE = self.directivity.size
        if self.srcmatch.size  != SIZE:
            return False
        if self.refltrack.size != SIZE:
            return False
        if self.freq.size      != SIZE:
            return False
        # else
        return True

    @staticmethod
    def from_source(vna_obj, source, port):
        if source.is_channel:
            return Corrections.from_channel  (vna_obj, source.index, port)
        if source.is_cal_group:
            return Corrections.from_cal_group(vna_obj, source.name,  port)
        # else?
        assert False
        return Corrections()
    @staticmethod
    def from_channel(vna_obj, channel, port):
        assert channel in vna_obj.channels
        assert vna_obj.channel(channel).is_calibrated
        term_scpi = f"SENS{channel}:CORR:CDAT? '{'{term}'}',{port},{port}"
        freq_scpi = f"SENS{channel}:CORR:STIM?"
        corrections = Corrections()
        corrections.directivity = vna_obj.query_64_bit_complex(term_scpi.format(term='DIRECTIVITY'))
        corrections.srcmatch    = vna_obj.query_64_bit_complex(term_scpi.format(term='SRCMATCH'   ))
        corrections.refltrack   = vna_obj.query_64_bit_complex(term_scpi.format(term='REFLTRACK'  ))
        corrections.freq        = vna_obj.query_64_bit(freq_scpi)
        return corrections

    @staticmethod
    def from_cal_group(vna_obj, cal_group, port):
        assert cal_group.lower() in vna_obj.cal_groups
        with TempChannel(vna_obj) as temp_channel:
            ch = vna_obj.channel(temp_channel.index)
            ch.cal_group = cal_group
            ch.dissolve_cal_group_link()
            return Corrections.from_channel(vna_obj, ch.index, port)
