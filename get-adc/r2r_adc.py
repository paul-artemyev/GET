import RPi.GPIO as GPIO, time

maxVoltage = 3.3

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    
    def set_number(self, number):
        binary = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, binary)
        return signal
    
    def sequential_counting_adc(self):
        while True:
            for value in range(256):
                signal = self.set_number(value)
                time.sleep(0.01)
                comparatorValue = GPIO.input(comparator)
                
                if comparatorValue == 0:
                    return maxVoltage
                
                return value
    
    def get_sc_voltage(self):
        digital_voltage = self.sequential_counting_adc()
        voltage = digital_voltage/256*self.dynamic_range

        return voltage

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.05)

        while True:
            voltage = adc.get_sc_voltage()
            print(voltage)
    
    finally:
        adc.deinit()