"""
LED example for Pico. Blinks external LED on and off.

REQUIRED HARDWARE:
* LED on pin GP14.
"""

# Created by: Daria Bernice Calitis
# Created on: Feb 2022

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
led.value = False

while True:
    led.value = not led.value
    time.sleep(1)
