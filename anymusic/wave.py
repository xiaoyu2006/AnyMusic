"""
Wave file manipulation.
"""

import wave

from anymusic.basic import scale
from .type import Audio


# pylint: disable=R0913
def write_file(
    filename: str,
    f: Audio,
    duration: float,
    framerate: int = 44100,  # 44.1 kHz
    sampwidth: int = 2,  # 16 bits
    progress_bar_interval: int | None = 50000,  # In frames
) -> None:
    """
    Writes a wave file. If `progress_bar_interval` is not `None`, then a progress bar will be printed to the console
    every `progress_bar_interval` frames.
    """
    # pylint: disable=E1101
    total_frames = int(duration * framerate)
    with wave.open(filename, "w") as file:
        file.setnchannels(1)
        file.setsampwidth(sampwidth)
        file.setframerate(framerate)
        file.setnframes(total_frames)
        for t in range(total_frames):
            amp = int(f(t / framerate) * (2 ** (sampwidth * 8 - 1) - 1))
            file.writeframesraw(amp.to_bytes(sampwidth, "little", signed=True))
            if progress_bar_interval is not None and t % progress_bar_interval == 0:
                print(f"Writing {t}/{total_frames} frames", end="\r")


# pylint: disable=R0913
def write_and_normalize_file(
    filename: str,
    f: Audio,
    duration: float,
    framerate: int = 44100,  # 44.1 kHz
    sampwidth: int = 2,  # 16 bits
    progress_bar_interval: int | None = 50000,  # In frames
) -> None:
    """
    A variant of write_file that normalizes the audio into [-1, 1] before writing.
    Note that it takes double the time as it tries to sample the entire Audio function into memory and find the maximum
    amplitude.
    """
    total_frames = int(duration * framerate)
    maximum = max(abs(f(t / framerate)) for t in range(total_frames))
    normalized = scale(f, 1 / maximum)
    write_file(filename, normalized, duration, framerate, sampwidth, progress_bar_interval)


def read_file(filename: str) -> Audio:
    """
    Reads a wave file. Note that it may take a lot of memory if the file is large.
    """
    with wave.open(filename, "r") as file:
        nchannels = file.getnchannels()
        sampwidth = file.getsampwidth()
        framerate = file.getframerate()
        nframes = file.getnframes()
        frames = file.readframes(nframes)
        return lambda t: int.from_bytes(
            frames[int(t * framerate) * nchannels * sampwidth : (int(t * framerate) + 1) * nchannels * sampwidth],
            "little",
            signed=True,
        ) / (2 ** (sampwidth * 8 - 1) - 1)
