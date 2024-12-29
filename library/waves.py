import numpy as np
from library.constants import RATE, BPM


def d2t(x): return x*60/BPM
def d2s(x): return int(x*RATE*60/BPM)


def fade_in_lin(arr, dur):
    assert (len(arr) >= d2s(dur))
    mul = np.concatenate(
        (np.linspace(0, 1, d2s(dur)), np.ones(len(arr)-d2s(dur))))
    return arr*mul


def fade_out_lin(arr, dur):
    return fade_in_lin(arr[::-1], dur)[::-1]


class Samples():
    def sine(freq, dur):
        return np.sin(2*np.pi*freq*np.linspace(0, d2t(dur), d2s(dur)))

    def square(freq, dur):
        return 1-(np.int16(2*freq*np.linspace(0, d2t(dur), d2s(dur))) % 2)*2

    def saw(freq, dur):
        return 1-((freq*np.linspace(0, d2t(dur), d2s(dur))) % 1)*2

    def white(freq, dur):
        return np.random.uniform(-1, 1, d2s(dur))

    def snap(freq, dur):
        x = np.zeros(d2s(dur))
        x[np.linspace(0, d2s(dur), int(d2t(dur)*freq)).astype(int)[:-1]] = 1
        return x

    def hi(freq, dur):
        return fade_out_lin(Samples.white(None, dur), dur)

    def saww(freq, dur):
        a = 50
        return Samples.saw(freq+a, dur)*Samples.sine(a, dur)

    def drum(freq, dur):
        return fade_out_lin(Samples.sine(freq, dur), dur)


def womp(arr, freq, dur):
    return arr*(Samples.sine(freq, dur)+1)/2


def line(notes, sample_func):
    return np.concatenate([np.zeros(d2s(d)) if n == None else sample_func(note(n), d) for n, d in notes])
