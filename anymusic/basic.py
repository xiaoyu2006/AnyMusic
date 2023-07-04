"""
Contains basic functions for generating sound waves.
"""

import math
import functools
from typing import Callable, TypeVar

from .type import Sec2Amp


R = TypeVar("R")
S = TypeVar("S")
T = TypeVar("T")


def sine(hz: float) -> Sec2Amp:
    """
    Returns a sine wave of the given frequency.
    """
    return lambda t: math.sin(t * hz * math.pi * 2)


def square(hz: float) -> Sec2Amp:
    """
    Returns a square wave of the given frequency.
    """
    return lambda t: 1 if math.sin(t * hz * math.pi * 2) > 0 else -1


def triangle(hz: float) -> Sec2Amp:
    """
    Returns a triangle wave of the given frequency.
    """
    return lambda t: 1 - abs((t * hz * 2) % 2 - 1) * 2


def stack(*fs: Sec2Amp) -> Sec2Amp:
    """
    Returns sum of the given functions.
    """
    return lambda t: functools.reduce(lambda x, y: x + y, [f(t) for f in fs])


def scale(f: Sec2Amp, factor: float) -> Sec2Amp:
    """
    Returns a scaled version of the given function.
    """
    return lambda t: f(t) * factor


def composition(f: Callable[[S], T], g: Callable[[R], S]) -> Callable[[R], T]:
    """
    Returns the composition of the given functions, that is, f(g(x)).
    """
    return lambda t: f(g(t))

def from_to(f: Sec2Amp, start: float, end: float) -> Sec2Amp:
    """
    Returns a function that is 0 before start and after end.
    """
    return lambda t: f(t) if start <= t <= end else 0
