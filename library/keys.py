from library.constants import *

# Major keys
C_MAJOR = [C4, D4, E4, F4, G4, A4, B4, C5]
G_MAJOR = [G4, A4, B4, C5, D5, E5, F5_SHARP, G5]
D_MAJOR = [D4, E4, F4_SHARP, G4, A4, B4, C5_SHARP, D5]
A_MAJOR = [A4, B4, C5_SHARP, D5, E5, F5_SHARP, G5_SHARP, A5]
E_MAJOR = [E4, F4_SHARP, G4_SHARP, A4, B4, C5_SHARP, D5_SHARP, E5]
F_MAJOR = [F4, G4, A4, BB4, C5, D5, E5, F5]
BB_MAJOR = [BB4, C5, D5, EB5, F5, G5, A5, BB5]

# Natural minor keys
A_MINOR = [A4, B4, C5, D5, E5, F5, G5, A5]
E_MINOR = [E4, F4_SHARP, G4, A4, B4, C5, D5, E5]
B_MINOR = [B4, C5_SHARP, D5, E5, F5_SHARP, G5, A5, B5]
F_SHARP_MINOR = [F4_SHARP, G4_SHARP, A4, B4, C5_SHARP, D5, E5, F5_SHARP]
C_SHARP_MINOR = [C4_SHARP, D4_SHARP, E4, F4_SHARP, G4_SHARP, A4, B4, C5_SHARP]
D_MINOR = [D4, E4, F4, G4, A4, BB4, C5, D5]
G_MINOR = [G4, A4, BB4, C5, D5, EB5, F5, G5]

# Dictionary mapping key names to their scale frequencies
KEYS = {
    'C': C_MAJOR,
    'G': G_MAJOR,
    'D': D_MAJOR,
    'A': A_MAJOR,
    'E': E_MAJOR,
    'F': F_MAJOR,
    'Bb': BB_MAJOR,

    'Am': A_MINOR,
    'Em': E_MINOR,
    'Bm': B_MINOR,
    'F#m': F_SHARP_MINOR,
    'C#m': C_SHARP_MINOR,
    'Dm': D_MINOR,
    'Gm': G_MINOR
}


def get_keys(key_name, octave=4):
    """Return the frequencies for a major key scale.

    Args:
        key_name: String name of the key (e.g., 'C', 'G', 'F')

    Returns:
        List of frequencies for the scale notes
    """
    return [freq * 2**(octave-4) for freq in KEYS.get(key_name)]
