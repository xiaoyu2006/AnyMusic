"""
Wave file manipulation.
"""

import wave
from .type import Sec2Amp


# pylint: disable=R0913
def write_file(
    filename: str,
    f: Sec2Amp,
    duration: float,
    framerate: int = 44100,
    nchannels: int = 1,
    sampwidth: int = 2,
) -> None:
    """
    Writes a wave file.
    """
    # pylint: disable=E1101
    with wave.open(filename, "w") as file:
        file.setnchannels(nchannels)
        file.setsampwidth(sampwidth)
        file.setframerate(framerate)
        file.setnframes(int(duration * framerate))
        for t in range(int(duration * framerate)):
            file.writeframesraw(
                int(f(t / framerate) * (2 ** (sampwidth * 8 - 1) - 1)).to_bytes(
                    sampwidth, "little", signed=True
                )
            )


def read_file(filename: str) -> Sec2Amp:
    """
    Reads a wave file.
    """
    with wave.open(filename, "r") as file:
        nchannels = file.getnchannels()
        sampwidth = file.getsampwidth()
        framerate = file.getframerate()
        nframes = file.getnframes()
        frames = file.readframes(nframes)
        return lambda t: int.from_bytes(
            frames[
                int(t * framerate)
                * nchannels
                * sampwidth : (int(t * framerate) + 1)
                * nchannels
                * sampwidth
            ],
            "little",
            signed=True,
        ) / (2 ** (sampwidth * 8 - 1) - 1)
