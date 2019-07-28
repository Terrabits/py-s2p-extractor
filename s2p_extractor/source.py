from enum import Enum

class Type(Enum):
    CHANNEL   = 'CHANNEL'
    CAL_GROUP = 'CAL_GROUP'
    def __str__(self):
        return self.value
    def __eq__(self, other):
        return str(other).upper() == str(self).upper()

class Source(object):
    def __init__(self, type=None, value=None):
        self.type      = type
        self.value     = value

    @property
    def is_channel(self):
        return self.type == Type.CHANNEL
    @property
    def index(self):
        assert self.is_channel
        return self.value
    @property
    def is_cal_group(self):
        return self.type == Type.CAL_GROUP
    @property
    def name(self):
        assert self.is_cal_group
        return self.value
