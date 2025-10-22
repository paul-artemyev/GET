import RPi.GPIO as GPIO, time


def f():
    bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
    comp_gpio = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(bits_gpio, GPIO.OUT, initial = 1)

    GPIO.output(bits_gpio, 0)
    GPIO.cleanup()


f()