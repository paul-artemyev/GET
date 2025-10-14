import mcp4725_driver as mcp, signal_generator as sg, time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = mcp.MCP4725(12, 10000, 3.290, True)
    
    while True:
        current_time = time.time()
        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_amplitude*amplitude
        number = dac.set_voltage(voltage)
        sg.wait_for_sampling_period(1/sampling_frequency)
finally:
    dac.deinit()