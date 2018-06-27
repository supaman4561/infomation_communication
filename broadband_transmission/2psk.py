import numpy as np
import matplotlib.pyplot as plt
from digitalmodulation import generate_psk

if __name__ == '__main__':
    SAMP = 128
    fc = 2
    t = np.arange(0, SAMP)
    signal = [1, -1, -1, -1, 1, 1, 1, -1]
    psk = generate_psk(signal, SAMP, fc)

    ### for demodulation 
    dem = []
    for i in signal:
        dem.extend(np.cos(2*np.pi*t/SAMP*fc))

    psk = np.array(psk)
    dem = np.array(dem)
    psk *= dem

    plt.subplot(212)
    plt.plot(range(len(psk)), psk)

    ### filtering
    psk = np.fft.fftshift(psk)
    psk = np.fft.fft(psk)
    psk = np.fft.fftshift(psk)

    psk[:512-16] = 0
    psk[512+16:] = 0

    psk = np.fft.fftshift(psk)
    psk = np.fft.fft(psk)
    psk = np.fft.fftshift(psk)

    plt.subplot(212)
    plt.plot(range(len(psk)), psk)
    plt.show()
