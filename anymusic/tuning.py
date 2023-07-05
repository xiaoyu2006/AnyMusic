"""
Make human-recognizable regular sounds.
"""

from .type import Tuning, Frequency


def equal_step_tuning(base_freq: Frequency, base: float, eqtm: float) -> Tuning:
    """
    Traditional music tuning systems use C * 2^( a + b * 1/12 ) as the frequency where it is the a * 12 + b semitones
    above the base frequency.
    However it can be further generalized to C * BASE^( a + b * EQTM ) where EQTM is the equal temperament.

    For example, for a 24-EDO scale, BASE is 2 and EQTM is 1/24.
    """
    return lambda a, b: base_freq * (base ** (a + b * eqtm))


def twelve_edo() -> Tuning:
    """
    Returns the traditional 12-EDO tuning.
    """
    # Starting from C0, the base frequency is 16.3 Hz.
    return equal_step_tuning(16.3, 2, 1 / 12)
