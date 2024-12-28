RATE = 44100
BPM = 80

# Reference octave (octave 4) frequencies in Hz
C4 = 261.63
C4_SHARP = DB4 = 277.18
D4 = 293.66
D4_SHARP = EB4 = 311.13
E4 = 329.63
F4 = 349.23
F4_SHARP = GB4 = 369.99
G4 = 392.00
G4_SHARP = AB4 = 415.30
A4 = 440.00
A4_SHARP = BB4 = 466.16
B4 = 493.88

# Octave 3 (one octave lower)
C3 = C4 / 2
C3_SHARP = DB3 = C4_SHARP / 2
D3 = D4 / 2
D3_SHARP = EB3 = D4_SHARP / 2
E3 = E4 / 2
F3 = F4 / 2
F3_SHARP = GB3 = F4_SHARP / 2
G3 = G4 / 2
G3_SHARP = AB3 = G4_SHARP / 2
A3 = A4 / 2
A3_SHARP = BB3 = A4_SHARP / 2
B3 = B4 / 2

# Octave 2 (two octaves lower)
C2 = C4 / 4
C2_SHARP = DB2 = C4_SHARP / 4
D2 = D4 / 4
D2_SHARP = EB2 = D4_SHARP / 4
E2 = E4 / 4
F2 = F4 / 4
F2_SHARP = GB2 = F4_SHARP / 4
G2 = G4 / 4
G2_SHARP = AB2 = G4_SHARP / 4
A2 = A4 / 4
A2_SHARP = BB2 = A4_SHARP / 4
B2 = B4 / 4

# Octave 1 (three octaves lower)
C1 = C4 / 8
C1_SHARP = DB1 = C4_SHARP / 8
D1 = D4 / 8
D1_SHARP = EB1 = D4_SHARP / 8
E1 = E4 / 8
F1 = F4 / 8
F1_SHARP = GB1 = F4_SHARP / 8
G1 = G4 / 8
G1_SHARP = AB1 = G4_SHARP / 8
A1 = A4 / 8
A1_SHARP = BB1 = A4_SHARP / 8
B1 = B4 / 8

# Octave 5 (one octave higher)
C5 = C4 * 2
C5_SHARP = DB5 = C4_SHARP * 2
D5 = D4 * 2
D5_SHARP = EB5 = D4_SHARP * 2
E5 = E4 * 2
F5 = F4 * 2
F5_SHARP = GB5 = F4_SHARP * 2
G5 = G4 * 2
G5_SHARP = AB5 = G4_SHARP * 2
A5 = A4 * 2
A5_SHARP = BB5 = A4_SHARP * 2
B5 = B4 * 2

# Octave 6 (two octaves higher)
C6 = C4 * 4
C6_SHARP = DB6 = C4_SHARP * 4
D6 = D4 * 4
D6_SHARP = EB6 = D4_SHARP * 4
E6 = E4 * 4
F6 = F4 * 4
F6_SHARP = GB6 = F4_SHARP * 4
G6 = G4 * 4
G6_SHARP = AB6 = G4_SHARP * 4
A6 = A4 * 4
A6_SHARP = BB6 = A4_SHARP * 4
B6 = B4 * 4

# Octave 7 (three octaves higher)
C7 = C4 * 8
C7_SHARP = DB7 = C4_SHARP * 8
D7 = D4 * 8
D7_SHARP = EB7 = D4_SHARP * 8
E7 = E4 * 8
F7 = F4 * 8
F7_SHARP = GB7 = F4_SHARP * 8
G7 = G4 * 8
G7_SHARP = AB7 = G4_SHARP * 8
A7 = A4 * 8
A7_SHARP = BB7 = A4_SHARP * 8
B7 = B4 * 8

__all__ = [
    'RATE', 'BPM',
    # Octave 1
    'C1', 'C1_SHARP', 'DB1',
    'D1', 'D1_SHARP', 'EB1',
    'E1',
    'F1', 'F1_SHARP', 'GB1',
    'G1', 'G1_SHARP', 'AB1',
    'A1', 'A1_SHARP', 'BB1',
    'B1',
    # Octave 2
    'C2', 'C2_SHARP', 'DB2',
    'D2', 'D2_SHARP', 'EB2',
    'E2',
    'F2', 'F2_SHARP', 'GB2',
    'G2', 'G2_SHARP', 'AB2',
    'A2', 'A2_SHARP', 'BB2',
    'B2',
    # Octave 3
    'C3', 'C3_SHARP', 'DB3',
    'D3', 'D3_SHARP', 'EB3',
    'E3',
    'F3', 'F3_SHARP', 'GB3',
    'G3', 'G3_SHARP', 'AB3',
    'A3', 'A3_SHARP', 'BB3',
    'B3',
    # Octave 4
    'C4', 'C4_SHARP', 'DB4',
    'D4', 'D4_SHARP', 'EB4',
    'E4',
    'F4', 'F4_SHARP', 'GB4',
    'G4', 'G4_SHARP', 'AB4',
    'A4', 'A4_SHARP', 'BB4',
    'B4',
    # Octave 5
    'C5', 'C5_SHARP', 'DB5',
    'D5', 'D5_SHARP', 'EB5',
    'E5',
    'F5', 'F5_SHARP', 'GB5',
    'G5', 'G5_SHARP', 'AB5',
    'A5', 'A5_SHARP', 'BB5',
    'B5',
    # Octave 6
    'C6', 'C6_SHARP', 'DB6',
    'D6', 'D6_SHARP', 'EB6',
    'E6',
    'F6', 'F6_SHARP', 'GB6',
    'G6', 'G6_SHARP', 'AB6',
    'A6', 'A6_SHARP', 'BB6',
    'B6',
    # Octave 7
    'C7', 'C7_SHARP', 'DB7',
    'D7', 'D7_SHARP', 'EB7',
    'E7',
    'F7', 'F7_SHARP', 'GB7',
    'G7', 'G7_SHARP', 'AB7',
    'A7', 'A7_SHARP', 'BB7',
    'B7',
]
