# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:22:51 2020

@author: Ahmad
"""
import numpy as np
from numpy import sqrt, real , imag
import matplotlib.pyplot as plt

x = [1+1j, 1-1j, -1+1j, -1-1j, 1+sqrt(3), -1-sqrt(3), (1+sqrt(3))*1j, (1+sqrt(3))*-1j]

plt.scatter(real(x), imag(x), c='r')
plt.grid(True, which="both")
plt.xlabel(r'$\mathbf{Inphase}$')
plt.ylabel(r'$\mathbf{Quadrature}$')
plt.title(r'$\mathbf{8-QAM\:Cross\:Constellation}$')
plt.axis('equal')

npx = np.real(x)
npy = np.imag(x)
d2 = npx**2+npy**2
#print(d2)
d4 = d2**2
#print(d4)
d6 = d2**3
#print(d6)

p = [1/8, 1/8]
# p = [0.1720, 0.0780] 
#print(p[0])
print(d2[0:4], d2[4:8])
exd2 = p[0]*sum(d2[0:4])+p[1]*sum(d2[4:8])
print('exd2 =', exd2)
exd4 = p[0]*sum(d4[0:4])+p[1]*sum(d4[4:8])
print("exd4 =", exd4)
exd6 = p[0]*sum(d6[0:4])+p[1]*sum(d6[4:8])
print("exd6 =", exd6)
kurr = (exd4/(exd2**2))
print("kurr =", kurr)
kurr3 = (exd6/(exd2**3))
print("kurr3 =", kurr3)
phi = kurr-2
print("phi =", phi)
si = kurr3-9*kurr+12
print("si =", si)
