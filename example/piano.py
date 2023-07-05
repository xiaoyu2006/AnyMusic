# pylint: disable=C0116, C0114

from typing import List
from anymusic.basic import stack, envelope
from anymusic.util import note_to_audio, fade_out_exp
from anymusic.timbre import default_piano
from anymusic.tuning import twelve_edo
from anymusic.type import Note, Audio, Envelope
from anymusic.wave import write_and_normalize_file


# Do, Re, Mi, Fa, Sol, La, Si
notes: List[Note] = [
    (4, 0, 0, 1),
    (4, 2, 1, 2),
    (4, 4, 2, 3),
    (4, 5, 3, 4),
    (4, 7, 4, 5),
    (4, 9, 5, 6),
    (4, 11, 6, 7),
]


def fade_out_effect(audio: Audio) -> Audio:
    multiplier: Envelope = fade_out_exp(1, 1.6)
    return envelope(audio, multiplier)


audios = [note_to_audio(note, twelve_edo(), default_piano(), fade_out_effect) for note in notes]
final_audio = stack(audios)
write_and_normalize_file("piano.wav", final_audio, 7)
