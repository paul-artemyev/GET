import time as t
import RPi.GPIO as GPIO

GPIO.setmode(BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.output(16, 0)
GPIO.output(12, 0)
GPIO.output(25, 0)
GPIO.output(17, 0)
GPIO.output(27, 0)
GPIO.output(23, 0)
GPIO.output(22, 0)
GPIO.output(24, 0)

GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(element) in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(up):
        num += 1
        print(num, dec2bin(num))
        t.sleep(sleep_time)
GPIO.setup(9, GPIO.IN)