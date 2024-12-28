import numpy as np
from scipy.io.wavfile import write
from library.waves import RATE
from library.constants import RATE, BPM


def write_wav(arr, name='test'):
    """Write a numpy array as a WAV file.

    Args:
        arr: numpy array of audio samples between -1 and 1
        name: filename to write to (without .wav extension)
    """
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
    scaled = np.float32(arr)
    sd.play(scaled, RATE)
    if blocking:
        sd.wait()
