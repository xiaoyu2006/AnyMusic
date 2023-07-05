"""
Different timbres.
"""

from typing import Iterable
from .basic import sine, square, triangle, sawtooth, stack, scale
from .type import Frequency, Audio, Timbre


def sine_timbre() -> Timbre:
    """
    Returns a timbre that uses sine waves.
    """
    return sine


def square_timbre() -> Timbre:
    """
    Returns a timbre that uses square waves.
    """
    return square


def triangle_timbre() -> Timbre:
    """
    Returns a timbre that uses triangle waves.
    """
    return triangle


def sawtooth_timbre() -> Timbre:
    """
    Returns a timbre that uses sawtooth waves.
    """
    return sawtooth


def piano(overtunes_multiplier: Iterable[float]) -> Timbre:
    """
    Returns a timbre that sounds like a piano.
    It has overtones proportional to base frequency for n in overtunes_multiplier.

    Note: overtunes_multiplier[0] should be 1 in most cases in order to preserve base frequency loudness.
    """

    def _piano(freq: Frequency) -> Audio:
        overtune_waves = [scale(sine(freq * i), multiplier) for i, multiplier in enumerate(overtunes_multiplier)]
        return stack(overtune_waves)

    return _piano


def default_piano() -> Timbre:
    """
    Returns a timbre that sounds like a electric piano.
    """
    multipliers = [1 / i for i in range(1, 8)]
    return piano(multipliers)
