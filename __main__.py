#!/usr/bin/env python
import numpy                              as     np
from   rohdeschwarz.instruments.vna       import Vna
from   s2p_extractor.corrections          import Corrections
from   s2p_extractor.s21_phase import fix as     fix_s21_phase
import skrf                               as     rf

# get corrections from vna
vna = Vna()
vna.open_tcp()
outer_channel = 1
inner_channel = 2
port          = 1
outer_corr = Corrections.from_vna(vna, outer_channel, port)
inner_corr = Corrections.from_vna(vna, inner_channel, port)

# frequencies must match
assert not False in outer_corr.freq == inner_corr.freq

# calculate s-parameters
d   = outer_corr.refltrack + (outer_corr.srcmatch * (inner_corr.directivity - outer_corr.directivity))
s11 =        (inner_corr.directivity - outer_corr.directivity) / d
s21 = np.sqrt(outer_corr.refltrack   * inner_corr.refltrack  ) / d
s22 = inner_corr.srcmatch - (outer_corr.srcmatch * inner_corr.refltrack) / d

# s21 phase is ambiguous after sqrt
# fix
freq = outer_corr.freq
s21  = fix_s21_phase(freq, s21)

# save result
s = []
for i in range(0, len(freq)):
    si = np.array([[s11[i], s21[i]], [s21[i], s22[i]]])
    s.append(si)
s = np.array(s)
z0 = np.array([50.0 + 0j, 50.0 + 0j], dtype=np.complex_)

network = rf.Network()
network.s  = s
network._frequency.f  = freq
network.z0 = z0
network.write_touchstone('test.s2p')
