#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

filename = input("filename:")
f = open(filename, 'r')
data = [int(v) for v in list(f.readline())]
result = []

for d in data:
    if d == 0 :
        result.extend([0,0,0,0])
    else :
        result.extend([0,1,1,0])

spectrum = np.abs(np.fft.fft(result))**2
t = np.arange(0, len(result))

plt.subplot(121)
plt.title("wave")
plt.plot(t, result)
plt.subplot(122)
plt.title("spectrums")
plt.plot(t, spectrum)

plt.show()

f.close()
