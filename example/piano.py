# pylint: disable=C0116, C0114

from typing import Tuple, List
from anymusic import default_piano, traditional_scale_system, write_file, from_to, stack, Octave, Semitone, Time, Audio

piano = default_piano()
scale = traditional_scale_system()

From = Time
To = Time
Note = Tuple[Octave, Semitone, From, To]

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


def note_to_audio(note: Note) -> Audio:
    oct, sem, from_, to = note  # pylint: disable=W0622
    freq = scale(oct, sem)
    audio = piano(freq)
    return from_to(audio, from_, to)


audios = [note_to_audio(note) for note in notes]
final_audio = stack(*audios)
write_file("piano.wav", final_audio, 7)
