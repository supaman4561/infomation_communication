import numpy as np
import matplotlib.pyplot as plt
from digitalmodulation import *

N = 128  # number of sampling points
fc = 4   # frequency of carrier wave
signal = input("signal=")
signal = [int(s!='0') for s in list(signal)]

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
