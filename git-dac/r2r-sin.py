import r2r_dac as r2r, signal_generator as sg, time

amplitude = 2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 5, True)
    
    while True:
        current_time = time.time()
        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_amplitude*amplitude
        number = dac.set_voltage(voltage)
        dac.set_number(number)
        sg.wait_for_sampling_period(1/sampling_frequency)
finally:
    dac.deinit()