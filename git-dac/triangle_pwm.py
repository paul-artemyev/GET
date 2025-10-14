import pwm_dac as pd, time, tr_generator as tg, time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = pd.PWM_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.05, True)
    
    while True:
        current_time = time.time()
        normalized_amplitude = tg.get_triangle_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_amplitude*amplitude
        number = dac.set_voltage(voltage)
        tg.wait_for_sampling_period(1/sampling_frequency)
finally:
    dac.deinit()