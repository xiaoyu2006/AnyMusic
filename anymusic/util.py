"""
Miscellaneous functions.
"""

from typing import Optional, Callable

from .basic import shift, strip
from .type import Envelope, Note, Timbre, Audio, Tuning, Time


def note_to_audio(
    note: Note, tuning: Tuning, timbre: Timbre, effect: Optional[Callable[[Audio], Audio]] = None
) -> Audio:
    """
    Returns the audio of the given note. It will be shifted and stripped to the given start and end time.
    """
    oct, sem, start, end = note  # pylint: disable=W0622
    audio = timbre(tuning(oct, sem))
    if effect is not None:
        audio = effect(audio)
    return strip(shift(audio, start), start, end)


def fade_out_linear(lasting: Time) -> Envelope:
    """
    Returns a linear fade out multiplier.
    """
    return lambda t: 1 - t / lasting

def fade_out_exp(lasting: Time, exp: float) -> Envelope:
    """
    Returns an exponential fade out multiplier.
    """
    return lambda t: (lasting - t) ** exp / lasting ** exp
