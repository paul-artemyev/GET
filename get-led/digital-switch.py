import RPi.GPIO as GPIO

GPIO.setmode(BCM)

GPIO.setup(16, GPIO.OUT)

button = 13

GPIO.setup(button, GPIO.IN)

state = 0

while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)