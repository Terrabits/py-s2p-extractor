import numpy       as np
from   pathlib import Path
from   s2p_extractor.corrections import Corrections
from   s2p_extractor.phase       import fix as fix_phase
import skrf        as rf

def calculate(vna_obj, outer_source, inner_source, port, filename, export_cal_data=False):
    # Get corrections
    outer_corr = Corrections.from_source(vna_obj, outer_source, port)
    inner_corr = Corrections.from_source(vna_obj, inner_source, port)

    # export corrections?
    if export_cal_data:
        cal_data_filename = str(Path(filename).parent / f'Port {port} cal data.npz')
        np.savez(cal_data_filename, **{
            'outer_corr.directivity': outer_corr.directivity,
            'outer_corr.srcmatch':    outer_corr.srcmatch,
            'outer_corr.refltrack':   outer_corr.refltrack,
            'outer_corr.freq':        outer_corr.freq,
            'inner_corr.directivity': inner_corr.directivity,
            'inner_corr.srcmatch':    inner_corr.srcmatch,
            'inner_corr.refltrack':   inner_corr.refltrack,
            'inner_corr.freq':        inner_corr.freq
        })

    # must have complete data sets
    assert     outer_corr.is_valid
    assert not outer_corr.is_empty
    assert     inner_corr.is_valid
    assert not inner_corr.is_empty
    # frequencies must match
    assert not False in outer_corr.freq == inner_corr.freq

    # calculate s-parameters
    d   = outer_corr.refltrack + (outer_corr.srcmatch * (inner_corr.directivity - outer_corr.directivity))
    s11 =        (inner_corr.directivity - outer_corr.directivity) / d
    s21 = np.sqrt(outer_corr.refltrack   * inner_corr.refltrack  ) / d
    s22 = inner_corr.srcmatch - (outer_corr.srcmatch * inner_corr.refltrack) / d

    # fix ambiguous s21 phase caused by sqrt
    freq = outer_corr.freq
    s21  = fix_phase(freq, s21)

    # save result
    s  = []
    for i in range(0, len(freq)):
        si = np.array([[s11[i], s21[i]], [s21[i], s22[i]]])
        s.append(si)
    s  = np.array(s)
    z0 = np.array([50.0 + 0j, 50.0 + 0j], dtype=np.complex_)

    network    = rf.Network()
    network.s  = s
    network._frequency.f = freq
    network.z0 = z0
    network.write_touchstone(filename)
