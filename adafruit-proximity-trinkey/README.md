adafruit-proximity-trinkey
==========================

Messing around with the Adafruit Proximity Trinkey.

All CircuitPython examples are on 9.0.0.alpha2 as of this writing.


Where Do I Get One?
-------------------

[Adafruit Proximity Trinkey](https://www.adafruit.com/product/5022 "Adafruit product page")


How Do I Get Started?
---------------------

[Adafruit Learn Guide for Proximity Trinkey ](https://learn.adafruit.com/adafruit-proximity-trinkey)


Projects
--------

### Dual-Load
Proximity trinkeys have two touch sensors, so we can use `supervisor.set_next_code_file` and `supervisor.reload` to pick which of two programs the Trinkey is going to run. Projects where I'm using this technique go under the CircuitPython/Dual-Load directory.

#### Spacebar-MIDI
Spacebar-MIDI is me managing to get two of the demo programs for CircuitPython to fit onto one Proximity Trinkey. I'm unduly proud that I got enough libraries for them both to work, to fit.
