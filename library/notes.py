from library.constants import *
from library.waves import fade_in_lin, fade_out_lin, d2s


def note(freq, dur, wave):
    return fade_in_lin(fade_out_lin(wave(freq, dur), .25), 0.1)


def rest(dur):
    return np.zeros(d2s(dur))
