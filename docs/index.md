# Index

*Music from the very basic.*

`AnyMusic` aims to be a Python library for creating *arbitrary* music.

The rough idea is to create a piece of `Audio` that maps `Time` to `Ampitude`, then save it to a wav file.

`AnyMusic` is written in a very functional manner, so it's easy to compose different parts together.

## Installation

The module is available on PyPI, sticks to the latest Python and has no dependencies.

``` sh
pip install anymusic
```

## Usage

Consider a simple sine wave:

``` py title="sine.py"
from anymusic.basic import sine
from anymusic.wave import write_file

a4 = sine(440)
write_file("a4.wav", a4, 6)
```

Raising pitch:

``` py title="raising.py"
from anymusic.basic import composition, sine
from anymusic.wave import write_and_normalize_file

def raising(t: float) -> float:
    return t**2

base = sine(40)
raising_audio = composition(base, raising)  # Easy composing!
write_and_normalize_file("raising.wav", raising_audio, 20)
```

And you can also use different timbres and tunings:

``` py title="timbre.py"
from anymusic.timbre import default_piano
from anymusic.tuning import twelve_edo
from anymusic.wave import write_and_normalize_file

piano = default_piano()
get_tune = twelve_edo()

c4 = piano(get_tune(4, 0))
write_and_normalize_file("piano-c4.wav", c4, 5)
```
