print("Version 3 installed using USB")
import time

import machine, neopixel

leds_number = 20
pin_led = 26

np = neopixel.NeoPixel(machine.Pin(pin_led), leds_number)

for i in range(4, leds_number - 5):
    np[i] = (25, 25, 75)
np.write()
