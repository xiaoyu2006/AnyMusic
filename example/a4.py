# pylint: disable=C0116, C0114

from anymusic.basic import sine, triangle, square, sawtooth
from anymusic.wave import write_file


A4_FREQ = 440

write_file("a4.wav", sine(A4_FREQ), 6)
write_file("a4_triangle.wav", triangle(A4_FREQ), 6)
write_file("a4_square.wav", square(A4_FREQ), 6)
write_file("a4_sawtooth.wav", sawtooth(A4_FREQ), 6)
