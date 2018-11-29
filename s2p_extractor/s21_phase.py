from numpy import angle, average, conj, pi, unwrap

def fix(freq, s21):
    return _fix_dc(freq, _fix_phase_jumps(s21))

def _fix_phase_jumps(s21):
    for i in range(1,len(s21)):
        delta = abs(angle(s21[i]*conj(s21[i-1])))
        if delta > pi/2.0:
            s21[i] = -1.0 * s21[i]
    return s21

def _middle_range(s21):
    points = len(s21)
    if points < 2:
        return range(0,0)
    if points < 7:
        return range(1, points)
    start  = int(0.2 * points) + 1
    stop   = int(0.8 * points)
    return range(start, stop)
# y = mx + b
# b = y - mx
# m = (y2 - y1) / (x2 - x1)
# b = y1 - m*x1
def _fix_dc(freq, s21):
    middle = _middle_range(s21)
    if not middle:
        return s21
    phases = unwrap(angle(s21))
    b_values = []
    for i in middle:
        m = (phases[i] - phases[i-1]) / (freq[i] - freq[i-1])
        b_values.append(phases[i] - m * freq[i])
    b_avg = average(b_values) % (2.0*pi)
    if b_avg > pi:
        b_avg = b_avg - 2.0 * pi
    if abs(b_avg) > pi/2.0:
        s21 = -1.0*s21
    return s21
