import board
import neopixel
import time

import adafruit_ad569x

i2c = board.I2C()
# dac = adafruit_ad569x.Adafruit_AD569x(i2c)

print("Hello World!")

RED = (127, 0, 0)
GREEN = (0, 127, 0)
BLUE = (0, 0, 127)
OFF = (0, 0, 0)


pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3)


while __name__ == '__main__':
    pixel.fill(RED)
    time.sleep(1)
    pixel.fill(GREEN)
    time.sleep(1)
    pixel.fill(BLUE)
    time.sleep(1)
    pixel.fill(OFF)
    time.sleep(1)

