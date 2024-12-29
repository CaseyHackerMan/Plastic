import numpy as np
from scipy.io.wavfile import write

RATE = 44100
BPM = 80
KEY = 0

d2t = lambda x: x*60/BPM
d2s = lambda x: int(x*RATE*60/BPM)
note = lambda n: 400*2**((n+KEY)/12)

def fade_in_lin(arr, dur):
    assert(len(arr) >= d2s(dur))
    mul = np.concatenate((np.linspace(0,1,d2s(dur)),np.ones(len(arr)-d2s(dur))))
    return arr*mul

def fade_out_lin(arr, dur):
    return fade_in_lin(arr[::-1],dur)[::-1]

class Samples():
    def sine(freq, dur):
        return np.sin(2*np.pi*freq*np.linspace(0,d2t(dur),d2s(dur)))

    def square(freq, dur):
        return 1-(np.int16(2*freq*np.linspace(0,d2t(dur),d2s(dur)))%2)*2

    def saw(freq, dur):
        return 1-((freq*np.linspace(0,d2t(dur),d2s(dur)))%1)*2

    def white(freq, dur):
        return np.random.uniform(-1, 1, d2s(dur))

    def snap(freq,dur):
        x = np.zeros(d2s(dur))
        x[np.linspace(0,d2s(dur),int(d2t(dur)*freq)).astype(int)[:-1]] = 1
        return x

    def hi(freq, dur):
        return fade_out_lin(Samples.white(None, dur), dur)

    def saww(freq, dur):
        a = 50
        return Samples.saw(freq+a,dur)*Samples.sine(a,dur)

    def drum(freq, dur):
        return fade_out_lin(Samples.sine(freq,dur),dur)
    
def womp(arr, freq, dur):
    return arr*(Samples.sine(freq, dur)+1)/2

def line(notes, sample_func):
    return np.concatenate([np.zeros(d2s(d)) if n == None else sample_func(note(n),d) for n,d in notes])

def write_wav(arr, name='test'):
    assert(np.all(-1 <= arr) and np.all(arr <= 1))
    scaled = np.int16(arr*32767)
    write(f'{name}.wav', RATE, scaled)
    print(f'Wrote to {name}.wav')

if __name__ == '__main__':
    for n in dir(Samples):
        if n[0] != '_':
            write_wav(np.tile(getattr(Samples,n)(note(0),.5),8), f'Samples/{n}')