"""
AnyMusic is a collection of tools to create theoretically any music from the very basics of sine
waves.
"""

from .basic import sine, square, triangle, stack, scale, composition, from_to
from .scale import really_generic_scale_system, traditional_scale_system
from .type import Sec2Amp, ScaleSystem
from .wave import write_file, read_file

__version__ = "0.0.0"
