import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

t_leds = [6, 16, 12, 25, 17, 27, 23, 22, 24]

for pin in t_leds:
    GPIO.setup(pin, GPIO.OUT)

for pin in t_leds:
    GPIO.output(pin, 0)

led =26

button = 13

GPIO.setup(button, GPIO.IN)

state = 0

while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)