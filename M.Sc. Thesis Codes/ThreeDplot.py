"""
Created on Mon Aug 26 11:23:57 2019

@author: Ahmad
"""

#import komm as k
import random as rnd
from math import sqrt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')



M = 16
#qam = k.QAModulation(M)
#qam=k.QAModulation(orders=(4, 2), base_amplitudes=(1.0, 2.0))
#x = list(qam.constellation)
#print(x)
#print(qam.labeling)
"""
plt.plot([np.real(x)],[np.imag(x)],'ro')
plt.xlabel('Inphase')
plt.ylabel('Quadrature')
plt.title('16-QAM Constellation Diagram')
plt.grid(True)
plt.axis([-8, 8, -8, 8])
plt.show()
"""
"""
npx = np.real(x)
npy = np.imag(x)
d = np.zeros(len(x))
for i in range(len(x)):
    d[i] = npx[i]**2+npy[i]**2
d = list(d)
d2 = list(set(d))
d2.sort()
print('d2 sorted values are:', d2)
num_prob = 0  # number of probabilities
for i in range(len(d2)):
    q = d.index(d2[i])
    #print(q)
    w = d.count(d2[i])
    print('number of', d2[i], '\'s is', w)
    n = 1
    Q = []
    while n < w:
        Q.append(q)
        q = d.index(d2[i], q+1, M)
        n += 1
    Q.append(q)
    print('Indexes of d2 =', d2[i], 'is', Q)
    num_prob += 1
print('number of probabilities is:', num_prob)
"""

dd = [complex(-1,1), complex(-1,-1), complex(1,-1), complex(1,1), complex(-3,-1), complex(-3,1), complex(-1,-3), complex(-1,3), complex(1,-3), complex(1,3), complex(3,-1), complex(3,1), complex(-3,-3), complex(-3,3), complex(3,-3), complex(3,3)]

x3 = np.real(dd)
y3 = np.imag(dd)
z3 = np.zeros(16)

dx = 1.7*np.ones(16)
dy = 1.7*np.ones(16)
#dz = [0.4590/4, 0.4590/4, 0.4590/4, 0.4590/4, 0.3455/8, 0.3455/8, 0.3455/8,
 #     0.3455/8, 0.3455/8, 0.3455/8, 0.3455/8, 0.3455/8, 0.1955/4,  0.1955/4,  0.1955/4,  0.1955/4]
dz = [0.6745/4, 0.6745/4, 0.6745/4, 0.6745/4, 0.2780/8, 0.2780/8, 0.2780/8,
      0.2780/8, 0.2780/8, 0.2780/8, 0.2780/8, 0.2780/8, 0.0475/4,  0.0475/4,  0.0475/4,  0.0475/4]


#ax1.bar3d(x3, y3, z3, dx, dy, dz)

colors = ['m', 'm', 'm', 'm', 'lime', 'lime', 'lime',
          'lime', 'lime', 'lime', 'lime', 'lime', 'c', 'c', 'c', 'c']
for i in range(0, 16):
       ax1.bar3d(x3[i], y3[i], z3[i], dx, dy, dz[i], alpha=0.5, color=colors[i])


ax1.set_xlabel('I')
ax1.set_ylabel('Q')
ax1.set_zlabel('Probability')

plt.show()
