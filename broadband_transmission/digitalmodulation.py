import numpy as np
import matplotlib.pyplot as plt

def generate_ask(signal, N, fc):
    ask = []
    t = np.arange(0, N)
    wave0 = np.sin(2 * np.pi * t/N * fc) * 0
    wave1 = np.sin(2 * np.pi * t/N * fc)
    for i in signal:
        if i == 0:
            ask.extend(wave0)
        else:
            ask.extend(wave1)
    return ask

def generate_fsk(signal, N, fc):
    fsk = []
    t = np.arange(0, N)
    wave0 = np.sin(2 * np.pi * t/N * fc/2)
    wave1 = np.sin(2 * np.pi * t/N * fc)
    for i in signal:
        if i == 0:
            fsk.extend(wave0)
        else:
            fsk.extend(wave1)
    return fsk

def generate_psk(signal, N, fc):
    psk = []
    t = np.arange(0, N)
    wave0 = np.sin(2 * np.pi * t/N * fc)
    wave1 = np.sin(2 * np.pi * t/N * fc + np.pi)
    for i in signal:
        if i == 1:
            psk.extend(wave0)
        else:
            psk.extend(wave1)
    return psk

if __name__ == '__main__':
    N = 128  # number of sampling points
    fc = 4   # frequency of carrier wave

    signal = [0, 1, 0, 1, 0, 1, 0, 1]

    ask = generate_ask(signal, N, fc)
    fsk = generate_fsk(signal, N, fc)
    psk = generate_psk(signal, N, fc)

    plt.subplot(221)
    plt.plot(range(len(signal)*N),
            [int(v) for inner in [list(str(i))*N for i in signal]
                    for v in inner])
    plt.title("signal")

    plt.subplot(222)
    plt.plot(range(len(ask)), ask)
    plt.title("ASK")

    plt.subplot(223)
    plt.plot(range(len(fsk)), fsk)
    plt.title("FSK")

    plt.subplot(224)
    plt.plot(range(len(psk)), psk)
    plt.title("PSK")

    plt.show()
