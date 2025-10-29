from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title('График зависимости напряжения на входе АЦП от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.ylim(0, max_voltage)
    plt.xlim(0, max(time))
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []

    for i in range(1, len(time)):
        period = time[i] - time[i-1]
        sampling_periods.append(period)
    
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.title('Зависимость напряжения от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()