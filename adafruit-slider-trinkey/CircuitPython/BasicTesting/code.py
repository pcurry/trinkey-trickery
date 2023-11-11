import board
import time

import touchio
import analogio
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 2, brightness=0.3)
pixels.fill((0,255,0))

fader = analogio.AnalogIn(board.A0)
touch = touchio.TouchIn(board.TOUCH)

while True:
    if touch.value:
        print("Registering touch")
        pixels.brightness = 0.7
    else:
        pixels.brightness = 0.3
    print(f"Fader value: {fader.value}")
    time.sleep(0.3)


