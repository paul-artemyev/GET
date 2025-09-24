import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

t_leds = [6, 16, 12, 25, 17, 27, 23, 22, 24]

for pin in t_leds:
    GPIO.setup(pin, GPIO.OUT)

for pin in t_leds:
    GPIO.output(pin, 0)


led = 26

GPIO.setup(led, GPIO.OUT)
state = 0
period = 1

while True:
    GPIO.output(led, state)
    state = not state
    time.sleep(period)