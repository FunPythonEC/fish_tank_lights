print("Version 3 installed using USB")
import time

import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(26), 29)

for i in range(0, 29):
    np[i] = (255, 255, 0)
np.write()
