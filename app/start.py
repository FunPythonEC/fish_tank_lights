print("Version 3 installed using USB")
import time

import machine, neopixel

leds_number = 25
pin_led = 26

np = neopixel.NeoPixel(machine.Pin(pin_led), leds_number)

for i in range(
    leds_number,
):
    np[i] = (75, 75, 100)
np.write()
