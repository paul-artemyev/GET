import RPi.GPIO as GPIO
import time

GPIO.setmode(BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

for pin in leds:
    GPIO.setup(pin, GPIO.OUT)

for pin in leds:
    GPIO.output(pin, 0)

light_time = 0.2

while True:
    for led in leds:
        GPIO.output(led, 1)
        time.sleep(light_time)
        GPIO.output(led, 0)
    for led in reversed(leds):
        GPIO.output(led, 1)
        time.sleep(light_time)
        GPIO.output(led, 0)