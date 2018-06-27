import numpy as np
import matplotlib.pyplot as plt
from digitalmodulation import generate_qpsk

if __name__ == '__main__':
    SAMP = 128
    fc = 2
    t = np.arnage(0, SAMP)
    signal = ["00", "10", "11", "01", "01", "10", "00", "11"]
    qpsk = generate_qpsk(signal, SAMP, fc)
