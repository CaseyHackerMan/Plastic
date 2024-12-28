from library.waves import (
    s_saww, s_white,
    fade_in_lin, fade_out_lin, d2s
)
from library.utils import (
    write_wav, play
)
from library.constants import *
from library.notes import note, rest
from library.keys import get_keys

import numpy as np

# Get A major scale
a_major = get_keys('A', 4)
a_major_octave_5 = get_keys('A', 5)

# Main melody pattern
n1 = note(a_major[3], 0.5, s_saww)
n1_long = note(a_major[3], 1.0, s_saww)
n2 = note(a_major[4], 0.5, s_saww)
n2_long = note(a_major[4], 1.0, s_saww)
n3 = note(a_major[5], 0.5, s_saww)
n4 = note(a_major[6], 0.5, s_saww)
n5 = note(a_major[7], 0.5, s_saww)
n6 = note(a_major_octave_5[1], 0.5, s_saww)
n7 = note(a_major_octave_5[2], 0.5, s_saww)

short_rest = np.zeros(d2s(0.25))
long_rest = np.zeros(d2s(0.5))

theme = np.concatenate((
    n1, n3, n4, n5, n4, n3, n2_long,
    long_rest,
    n2, n3, n4, n5, n4, n3, n1_long,
    long_rest
))

play(theme)
write_wav(theme, 'mia_sebastian_theme')
