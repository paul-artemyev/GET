import RPi.GPIO as GPIO

dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setmode(GPIO.BCM)

for pin in dac_bits:
    GPIO.setup(pin, GPIO.OUT)

dynamic_range = 3.05

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В")
        return 0
    
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    binary = [int(element) for element in bin(number)[2:].zfill(8)]
    GPIO.output(dac_bits, binary)

try:
    while True:
        try:
            voltage = float(input("Ведите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()