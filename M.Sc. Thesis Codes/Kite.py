# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:33:38 2020

@author: Ahmad
"""

import os
from numpy import pi, exp, log, sqrt, concatenate, sum, real, imag, cos, sin
from numpy import array as arr
import matplotlib.pyplot as plt

# teta=[]
# for i in range(8):
#     teta.append(pi/8+i*pi/4)
# print(teta)    
# print(log(exp(1)))
# r1 = sqrt(log(8/7))

#print(r1)
# r2 = sqrt(log(8/5))
r2 = 0.16030724649592012
beta=0.6302
r1 = beta*r2
#print(r2)
# teta=arr(teta)
x1=[]
x2=[]
for i in range(8):
    x1.append(r1*exp(1j*((pi/4)*i+(pi/4))))
    x2.append(r2*exp(1j*((pi/4)*i+(3*pi/8))))
    # x1=(r1*exp(1j*teta))
x=concatenate([x1,x2])
# print(x)
# print(abs(x))
# print(sum(x))
# plt.plot(real(x1), imag(x1),'c-')
# plt.plot(real(x2), imag(x2),'c-')
circle1=plt.Circle((0, 0), r1, color='b', linestyle='--', fill=False)
circle2=plt.Circle((0, 0), r2, color='b', linestyle='--', fill=False)
ax = plt.gca()
# hold='True'
# ax.plot((0), (0), 'o', color='y')
ax.add_artist(circle1)
ax.add_artist(circle2)
plt.scatter(real(x), imag(x),c='red')
plt.grid(True, which="both")
plt.xlabel(r'$\mathbf{Inphase}$')
plt.ylabel(r'$\mathbf{Quadrature}$')
plt.title(r'$\mathbf{Geometrically\:Shaped\:Constellation}$')
plt.axis('equal')
# plt.xlim(-0.6, 0.6)
# plt.ylim(-0.8, 0.8)
# plt.show()
absFilePath = os.path.abspath(__file__)
os.chdir(os.path.dirname(absFilePath))
plt.savefig('GS2.eps')

si1=beta**2-2*beta*cos(pi/8)
print('psi1=', si1)
si2=beta*sin(pi/8)
print('psi2=', si2)
