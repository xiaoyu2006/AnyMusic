# Index

*Music from the very basic.*

AnyMusic aims to be a Python library for creating *arbitrary* music.

The rough idea is to create a piece of `Audio` that maps `Time` to `Ampitude`, then save it to a wav file.

The module is written in a very functional style, so it's easy to compose different parts together.

For example:

``` py
from anymusic.basic import sine
from anymusic.wave import write_file

a4 = sine(440)
write_file("a4.wav", a4, 6)
```
