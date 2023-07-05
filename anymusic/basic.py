"""
Contains basic functions for generating and manipulating sound waves.
"""

import math
import functools
from typing import Callable, TypeVar, Iterable

from .type import Audio, Frequency, Time


def sine(freq: Frequency) -> Audio:
    """
    Returns a sine wave of the given frequency.
    """
    return lambda t: math.sin(t * freq * math.pi * 2)


def square(freq: Frequency) -> Audio:
    """
    Returns a square wave of the given frequency.
    """
    return lambda t: 1 if math.sin(t * freq * math.pi * 2) > 0 else -1


def triangle(freq: Frequency) -> Audio:
    """
    Returns a triangle wave of the given frequency.
    """
    return lambda t: 1 - abs((t * freq * 2) % 2 - 1) * 2


def stack(fs: Iterable[Audio]) -> Audio:
    """
    Returns sum of the given functions.
    """
    return lambda t: functools.reduce(lambda x, y: x + y, [f(t) for f in fs])


def envelope(f: Audio, multiplier: Callable[[Time], float]) -> Audio:
    """
    Returns a function that is the given function multiplied by the given envelope.
    """
    return lambda t: f(t) * multiplier(t)


def scale(f: Audio, factor: float) -> Audio:
    """
    Returns a scaled version of the given function.
    """

    def constant(_: Time) -> float:
        return factor

    return envelope(f, constant)


R = TypeVar("R")
S = TypeVar("S")
T = TypeVar("T")


def composition(f: Callable[[S], T], g: Callable[[R], S]) -> Callable[[R], T]:
    """
    Returns the composition of the given functions, that is, f(g(x)).
    """
    return lambda t: f(g(t))


def strip(f: Audio, start: Time, end: Time) -> Audio:
    """
    Returns a function that is 0 before start and after end.
    """
    return lambda t: f(t) if start <= t <= end else 0


def shift(f: Audio, offset: Time) -> Audio:
    """
    Returns a function that is shifted by the given offset.
    """
    return lambda t: f(t - offset)
