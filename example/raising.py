# pylint: disable=C0116, C0114

from anymusic.basic import composition, sine
from anymusic.wave import write_file


def raising(t: float) -> float:
    return t**2


base = sine(40)
raising_audio = composition(base, raising)
write_file("raising.wav", raising_audio, 20)
