import board
import neopixel
import time

import adafruit_mcp9808

RED = (127, 0, 0)
GREEN = (0, 127, 0)
BLUE = (0, 0, 127)
OFF = (0, 0, 0)


pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3)

mcp = adafruit_mcp9808.MCP9808(board.I2C())


while __name__ == '__main__':
    pixel.fill(RED)
    print('Temperature: {} degrees C'.format(mcp.temperature))
    time.sleep(1)
    pixel.fill(GREEN)
    print('Temperature: {} degrees C'.format(mcp.temperature))
    time.sleep(1)
    pixel.fill(BLUE)
    print('Temperature: {} degrees C'.format(mcp.temperature))
    time.sleep(1)
    pixel.fill(OFF)
    print('Temperature: {} degrees C'.format(mcp.temperature))
    time.sleep(1)
