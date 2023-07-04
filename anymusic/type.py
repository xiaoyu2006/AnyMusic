"""
Common types.
"""

from typing import Callable

# Time |-> Amplitude
# Where Time is in seconds and Amplitude is in [-1, 1]
Sec2Amp = Callable[[float], float]

# Octaves, Semitones |-> Frequency
# Where Octaves is the number of octaves above the base frequency and Semitones is the number of
# semitones above the current octave.
ScaleSystem = Callable[[float, float], float]
