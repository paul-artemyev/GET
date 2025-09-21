import RPi.GPIO as GPIO
import time

GPIO.setmode(BCM)

led = 26

GPIO.setup(led, GPIO.OUT)
state = 0
period = 1

while True:
    GPIO.output(led, state)
    state = not state
    time.sleep(period)