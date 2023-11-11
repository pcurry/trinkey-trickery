import board
import neopixel
import time

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.3)
pixels[0] = RED
pixels[1] = GREEN
pixels[2] = BLUE
pixels[3] = OFF
time.sleep(2)


def cycle_pixels(sleep_time=1):
    buffer = pixels[0]
    pixels[0] = pixels[1]
    pixels[1] = pixels[2]
    pixels[2] = pixels[3]
    pixels[3] = buffer
    time.sleep(sleep_time)

while __name__ == '__main__':
    cycle_pixels()
