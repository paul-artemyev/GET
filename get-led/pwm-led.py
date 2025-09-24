import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

t_leds = [16, 12, 25, 17, 27, 23, 22, 24]

for pin in t_leds:
    GPIO.setup(pin, GPIO.OUT)

for pin in t_leds:
    GPIO.output(pin, 0)

led = 26

GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0