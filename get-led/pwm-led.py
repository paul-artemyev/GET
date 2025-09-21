import RPi.GPIO as GPIO
import time

GPIO.setmode(BCM)

led = 10

pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0