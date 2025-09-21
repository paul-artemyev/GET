import RPi.GPIO as GPIO

GPIO.setmode(BCM)

led = 16

GPIO.setup(led, GPIO.OUT)

state = 0

res = GPIO(state, GPIO.OUT)

while True:
    GPIO(led, not res)
    res = GPIO(state, GPIO.OUT)  