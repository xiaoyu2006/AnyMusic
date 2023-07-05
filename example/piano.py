# pylint: disable=C0116, C0114

from typing import Tuple, List
from anymusic.basic import stack, strip

from anymusic.timbre import default_piano
from anymusic.tuning import twelve_edo
from anymusic.type import Audio, Octave, Semitone, Time
from anymusic.wave import write_file

piano = default_piano()
scale = twelve_edo()

Note = Tuple[Octave, Semitone, Time, Time]

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
    oct, sem, start, end = note  # pylint: disable=W0622
    freq = scale(oct, sem)
    audio = piano(freq)
    return strip(audio, start, end)


audios = [note_to_audio(note) for note in notes]
final_audio = stack(*audios)
write_file("piano.wav", final_audio, 7)
