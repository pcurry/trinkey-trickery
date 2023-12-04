import board
import neopixel
import time

import adafruit_sgp30


STEMMA = board.STEMMA_I2C()


# Primary colors to cycle
RED = (127, 0, 0)
GREEN = (0, 127, 0)
BLUE = (0, 0, 127)
OFF = (0, 0, 0)


pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3)


sgp30 = adafruit_sgp30.Adafruit_SGP30(STEMMA)

print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.set_iaq_baseline(0x8973, 0x8AAE)
sgp30.set_iaq_relative_humidity(celsius=22.1, relative_humidity=44)


elapsed_sec = 0

while __name__ == '__main__':
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    pixel.fill(RED)
    time.sleep(1)
    elapsed_sec += 1
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))

    pixel.fill(GREEN)
    time.sleep(1)
    elapsed_sec += 1
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))

    pixel.fill(BLUE)
    time.sleep(1)
    elapsed_sec += 1
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))

    pixel.fill(OFF)
    time.sleep(1)
    elapsed_sec += 1
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))

    if elapsed_sec > 10:
        elapsed_sec = 0
        print(
            "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
            % (sgp30.baseline_eCO2, sgp30.baseline_TVOC)
        )
