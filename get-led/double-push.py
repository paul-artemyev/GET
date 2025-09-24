import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

for pin in leds:
    GPIO.setup(pin, GPIO.OUT)

for pin in leds:
    GPIO.output(pin, 0)

up_button = 9
down_button = 10

GPIO.setup(up_button, GPIO.IN)
GPIO.setup(down_button, GPIO.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(up_button) > 0:
        time.sleep(0.1)
        if GPIO.input(down_button) > 0:
            for pin in leds:
                GPIO.output(pin, 1)
        if num < 255:
            num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    
    if GPIO.input(down_button) > 0:
        time.sleep(0.1)
        if GPIO.input(up_button) > 0:
            for pin in leds:
                GPIO.output(pin, 1)
        if num < 255:
            num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    binary_value = dec2bin(num)
    for i in range(8):
        GPIO.output(leds[i], binary_value[i])