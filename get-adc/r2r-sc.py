from matplotlib import pyplot as plt
import time, r2r_adc, adc_plot

adc = r2r_adc.R2R_ADC()

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.time()

    while(time.time() - start_time < duration):
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(time.time() - start_time)

    adc_plot.plot_voltage_vs_time()
finally:
    r2r_adc.R2R_ADC.deinit()