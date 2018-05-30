#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

filename = input("filename:")
f = open(filename, 'r')
data = [int(v) for v in list(f.readline())]
result = []
minus_flag = False

for d in data:
    if d == 0 :
        result.extend([0,0,0,0])
    elif minus_flag == False:
        result.extend([1,1,0,0])
        minus_flag = True
    else :
        result.extend([-1, -1, 0, 0])
        minus_flag = False

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
