"""
Common types.
"""

from typing import Callable, Tuple

Time = float  # In seconds
Amp = float  # In [-1, 1]
Frequency = float  # In Hz
Octave = int  # In octaves (but not necessarily the traditional 12-EDO)
Semitone = int  # In semitones, [0, x-EDO]

# Time |-> Amplitude
# Where Time is in seconds and Amplitude is in [-1, 1]
# TODO: Audio does not carry the infomation of length.
Audio = Callable[[Time], Amp]

# Octaves, Semitones |-> Frequency
# Where Octaves is the number of octaves above the base frequency and Semitones is the number of semitones above the
# current octave.
Tuning = Callable[[Octave, Semitone], Frequency]

# Frequency |-> Sec2Amp
# Where Frequency is the base frequency of the wave.
Timbre = Callable[[Frequency], Audio]

# Time |-> Scalar
Envelope = Callable[[Time], float]

# Holds the information of a note.
# Octave, Semitone, Start, End
Note = Tuple[Octave, Semitone, Time, Time]
