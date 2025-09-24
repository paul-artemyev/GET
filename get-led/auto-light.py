import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

t_leds = [16, 12, 25, 17, 27, 23, 22, 24]

for pin in t_leds:
    GPIO.setup(pin, GPIO.OUT)

for pin in t_leds:
    GPIO.output(pin, 0)

led = 26

GPIO.setup(led, GPIO.OUT)

t_pin = 6

GPIO.setup(t_pin, GPIO.IN)

while True:
    res = GPIO.input(t_pin)
    GPIO.output(led, not res)