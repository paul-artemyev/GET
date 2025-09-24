import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

t_leds = [13, 26, 6, 16, 12, 25, 17, 27, 23, 22, 24]

for pin in t_leds:
    GPIO.setup(pin, GPIO.OUT)




leds = [24, 22, 23, 27, 17, 25, 12, 16]

for led in t_leds:
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
