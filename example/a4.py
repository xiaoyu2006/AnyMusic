# pylint: disable=C0116, C0114

from anymusic import sine, write_file

a4 = sine(440)
write_file("a4.wav", a4, 6)
