print("Version 3 installed using USB")
import time

import machine, neopixel

leds_number = 30
pin_led = 26

np = neopixel.NeoPixel(machine.Pin(pin_led), leds_number)

for i in range(0, leds_number):
    np[i] = [0, 0, 0]

for i in range(0, leds_number - 20):
    np[i] = (25, 25, 75)
np.write()
