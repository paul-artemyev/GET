import time

def get_triangle_wave_amplitude(freq, time):
    phase = (freq * time) % 1.0
    if phase < 0.5:
        return 2 * phase
    else:
        return 2 * (1 - phase)

def wait_for_sampling_period(sampling_frequency):
    time.sleep(sampling_frequency)