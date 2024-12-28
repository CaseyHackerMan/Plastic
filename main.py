from library.waves import (
    s_saww, s_white,
    fade_in_lin, fade_out_lin, d2s
)
from library.utils import (
    write_wav, play
)
from library.constants import *
from library.notes import note, rest

import numpy as np

a = note(A2, .5, s_saww)
b = note(B2, .5, s_saww)

rest = np.zeros(d2s(.5))
x = np.concatenate((rest, a, a, a, a, a, a, rest, b, b, b, a, a, a, a, rest))

play(x)
write_wav(x, 'beat')
