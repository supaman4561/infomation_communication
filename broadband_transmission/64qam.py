import numpy as np
import matplotlib.pyplot as plt
import math

def split_by_len(str, length):
    return [str[i:i+length] for i in range(0, len(str), length)]

def generate_64qam(signal, SAMP, fc):
    qam = []
    t = np.arange(0, SAMP)
    wave = []
    for i in range(64):
        if i % 2 == 0:
            amp = 0.5
        else:
            amp = 1
        wave.append(amp * np.exp(1j * (fc * np.pi * t/SAMP + math.floor(i/2) * np.pi/2)))

    signal = split_by_len(signal, 3)
    for s in signal:
        qam.extend(wave[int('0b' + s, 0)])

    qam = np.array(qam)
    return qam

if __name__ == '__main__':
    signal = "001100000011101110"
    SAMP = 128
    fc = 4
    qam = generate_8qam(signal, SAMP, fc)

    plt.plot(range(len(qam)), qam)
    plt.show()
