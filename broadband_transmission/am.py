import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    SAMPLING = 128
    carrier_frec = 32
    trans_frec = 4

    t = np.arange(0, SAMPLING)
    trans_wave = np.cos(2*np.pi*trans_frec*t/SAMPLING)

    modulated_wave = (trans_wave + 1) * np.cos(2*np.pi*carrier_frec*t/SAMPLING)

    spectrum = np.abs(np.fft.fft(modulated_wave))

    plt.subplot(121)
    plt.title("modulated_wave")
    plt.plot(t, modulated_wave)

    plt.subplot(122)
    plt.title("spectrum")
    plt.plot(t, spectrum)
    plt.show()
