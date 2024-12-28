import numpy as np
from scipy.io.wavfile import write

RATE = 44100
BPM = 80


def d2t(x): return x*60/BPM
def d2s(x): return int(x*RATE*60/BPM)


def s_sine(freq, dur):
    return np.sin(2*np.pi*freq*np.linspace(0, d2t(dur), d2s(dur)))


def s_square(freq, dur):
    return 1-(np.int16(2*freq*np.linspace(0, d2t(dur), d2s(dur))) % 2)*2


def s_saw(freq, dur):
    return 1-((freq*np.linspace(0, d2t(dur), d2s(dur))) % 1)*2


def s_white(dur):
    return np.random.uniform(-1, 1, d2s(dur))


def fade_in_lin(arr, dur):
    assert (len(arr) >= d2s(dur))
    mul = np.concatenate(
        (np.linspace(0, 1, d2s(dur)), np.ones(len(arr)-d2s(dur))))
    return arr*mul


def fade_out_lin(arr, dur):
    return fade_in_lin(arr[::-1], dur)[::-1]


def s_saww(freq, dur):
    return s_saw(freq, dur)*s_sine(50, dur)


def write_wav(arr, name='test'):
    scaled = np.int16(arr*32767)
    write(f'{name}.wav', RATE, scaled)
    print(f'Wrote to {name}.wav')


def play(arr, blocking=True):
    """
    Play an audio array live through speakers
    Args:
        arr: numpy array of audio samples
        blocking: if True, wait until playback is finished
    """
    import sounddevice as sd
    scaled = np.float32(arr)  # sounddevice expects float32 between -1 and 1
    sd.play(scaled, RATE)
    if blocking:
        sd.wait()  # Wait until the audio is finished playing
