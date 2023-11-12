import board
import neopixel
import time
import touchio

clockwise = touchio.TouchIn(board.TOUCH1)
ccw = touchio.TouchIn(board.TOUCH2)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.3)
pixels[0] = OFF
pixels[1] = RED
pixels[2] = GREEN
pixels[3] = BLUE
time.sleep(1)


def cycle_pixels(direction=1):
    if direction < 0:
        buffer = pixels[3]
        pixels[1:] = pixels[0:3]
        pixels[0] = buffer
    else:
        buffer = pixels[0]
        pixels[0:3] = pixels[1:]
        pixels[3] = buffer


is_main = __name__ == '__main__'
direction = 1

while is_main:
    if clockwise.value:
        direction = -1
    elif ccw.value:
        direction = 1
    else:
        pass
    cycle_pixels(direction)
    time.sleep(0.5)

