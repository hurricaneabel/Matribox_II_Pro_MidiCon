"""
Nomes dos ritmos disponíveis na bateria da Matribox II Pro.

Cada número corresponde ao valor MIDI enviado pelo CC 94.
Os valores começam em 0 e terminam em 99.
"""

from __future__ import annotations


DRUM_RHYTHMS: dict[int, str] = {
    0: "Rock 1",
    1: "Rock 2",
    2: "Rock 3",
    3: "Rock 4",
    4: "Rock 5",
    5: "Classic Rock 1",
    6: "Classic Rock 2",
    7: "Classic Rock 3",
    8: "Hard Rock",
    9: "Garage Rock",
    10: "Prog Rock",
    11: "Surf Rock",
    12: "Rock 5/4",
    13: "Post Rock 1",
    14: "Post Rock 2",
    15: "Post Rock 3",
    16: "Punk 1",
    17: "Punk 2",
    18: "Punk 3",
    19: "Punk 4",
    20: "Emo",
    21: "Grunge",
    22: "New Wave",
    23: "Post Punk 1",
    24: "Post Punk 2",
    25: "Hardcore",
    26: "Metal 1",
    27: "Metal 2",
    28: "Nu-Metal 1",
    29: "Nu-Metal 2",
    30: "Blues 1",
    31: "Blues 2",
    32: "Blues 3",
    33: "Blues 4",
    34: "Swing",
    35: "Shuffle",
    36: "Shuffle 3/4",
    37: "Bluegrass",
    38: "Country",
    39: "Folk",
    40: "Funk 1",
    41: "Funk 2",
    42: "Funk 3",
    43: "Funk 4",
    44: "Jazz Funk 1",
    45: "Jazz Funk 2",
    46: "Jazz Funk 3",
    47: "Jazz 1",
    48: "Jazz 2",
    49: "Jazz 3",
    50: "Jazz 4",
    51: "Bossanova 1",
    52: "Bossanova 2",
    53: "Fusion",
    54: "Pop 1",
    55: "Pop 2",
    56: "Pop 3",
    57: "Hip Hop 1",
    58: "Hip Hop 2",
    59: "Hip Hop 3",
    60: "Hip Hop Rock",
    61: "Pub",
    62: "Electro 1",
    63: "Electro 2",
    64: "Electronic Pop",
    65: "Techno",
    66: "Trip-Hop",
    67: "Break Beat",
    68: "Drum & Bass",
    69: "Latin 1",
    70: "Latin 2",
    71: "Latin 3",
    72: "Latin Pop 1",
    73: "Latin Pop 2",
    74: "Samba",
    75: "Tango",
    76: "Beguine",
    77: "Ska",
    78: "Polka",
    79: "Waltz",
    80: "Reggae 1",
    81: "Reggae 2",
    82: "Mazuke",
    83: "Musette",
    84: "March 1",
    85: "March 2",
    86: "March 3",
    87: "New Age 1",
    88: "New Age 2",
    89: "World",
    90: "Metronome 1/4",
    91: "Metronome 2/4",
    92: "Metronome 3/4",
    93: "Metronome 4/4",
    94: "Metronome 5/4",
    95: "Metronome 6/4",
    96: "Metronome 7/4",
    97: "Metronome 6/8",
    98: "Metronome 7/8",
    99: "Metronome 9/8",
}


def get_drum_rhythm_name(rhythm: int) -> str:
    """
    Retorna o nome correspondente ao número do ritmo.

    Args:
        rhythm:
            Número MIDI do ritmo, entre 0 e 99.

    Raises:
        ValueError:
            Quando o número informado não existe.
    """
    if rhythm not in DRUM_RHYTHMS:
        raise ValueError("O ritmo deve estar entre 0 e 99.")

    return DRUM_RHYTHMS[rhythm]