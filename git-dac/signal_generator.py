import numpy, time

def get_sin_wave_amplitude(freq, time):
    return 1 + numpy.sin(2*numpy.pi*freq*time)

def wait_for_sampling_period(sampling_frequency):
    time.sleep(sampling_frequency)