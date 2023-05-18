import numpy as math
import time
import matplotlib.pyplot as plt
import warnings
from matplotlib import MatplotlibDeprecationWarning
from tabulate import tabulate
warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)


amountSum, amountMultiplication = 0, 0


def random_signal():
    return math.random.uniform(-1, 1)


def fast_fourier_transform(f):
    global amountSum, amountMultiplication
    n = len(f)
    if n == 1:
        return f
    else:
        even, odd = fast_fourier_transform(f[::2]), fast_fourier_transform(f[1::2])
        factor = math.exp(-2j * math.pi * math.arange(n) / n)
        amountSum += 2
        amountMultiplication += 3
        return math.concatenate([even + factor[:n // 2] * odd, even + factor[n // 2:] * odd])


def plot_amplitude_spectrum(amplitude_spectrum, amount_input):
    fig2, ax2 = plt.subplots(figsize=(10, 10))
    ax2.set_title('Графік спектр амплітуд', fontsize=16)
    plt.grid(True)
    for i in range(0, amount_input):
        plt.plot(i, amplitude_spectrum[i], 'go-')
        plt.plot([i, i], [0, amplitude_spectrum[i]], 'g-',)
    plt.xlabel('k')
    plt.ylabel('|C_k|')
    plt.show()


def plot_phase_spectrum(phase_spectrum, amount_input):
    fig2, ax2 = plt.subplots(figsize=(10, 10))
    ax2.set_title('Графік спектр фаз', fontsize=16)
    plt.grid(True)
    for i in range(0, amount_input - 1):
        plt.plot(i, phase_spectrum[i], 'go-')
        plt.plot([i, i], [0, phase_spectrum[i]], 'g-')
    plt.xlabel('k')
    plt.ylabel('arg(C_k)')
    plt.show()
    return 0


def print_message():
    data = []
    headers = ["k", "C_k"]
    for i in range(amount_input):
        data.append([i, "{:.15f}".format(C_ks[i])])
    table = tabulate(data, headers, tablefmt="fancy_grid")
    print(table)

    print("\nЗагальний час обчислення коефіцієнтів:", time)
    print("Загальна кількість операцій додавання:", amountSum)
    print("Загальна кількість операцій множення:", amountMultiplication)

    amplitude_spectrum = []
    phase_spectrum = []
    for k in range(0, amount_input):
        amplitude_spectrum.append(abs(C_ks[k]))
        phase_spectrum.append(math.angle(C_ks[k]))

    # побудова графіку спектру амплітуд
    plot_amplitude_spectrum(amplitude_spectrum, amount_input)

    # побудова графіку спектру фаз
    plot_phase_spectrum(phase_spectrum, amount_input)


n = 8
amount_input = 2 ** n
func = [random_signal() for _ in range(amount_input)]
start = time.time()
C_ks = fast_fourier_transform(func)
time = time.time() - start
print_message()
