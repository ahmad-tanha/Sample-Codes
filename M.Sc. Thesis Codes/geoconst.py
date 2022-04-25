import os
import numpy as np
from numpy import pi, exp, sin, conj, random
import matplotlib.pyplot as plt
arr = np.array

x = [complex(0, 0), complex(0.5695, 0.1025), complex(0.1960, 0.5444), complex(-0.3735, 0.4419), complex(-0.5695, -0.1025), complex(-0.1960, -0.5444), complex(0.3735, -0.4419), complex(1.2468, 0),
     complex(0.9551, 0.8014), complex(0.2165, 1.2279), complex(-0.6234, 1.0798), complex(-1.1716, 0.4264), complex(-1.1716, -0.4264), complex(-0.6234, -1.0798), complex(0.2165, -1.2279), complex(0.9551, -0.8014)]
npx = arr(np.real(x))
npy = arr(np.imag(x))
plt.scatter(npx, npy, c='red')
""" fig, ax = plt.subplots()
fig = plt.gcf()
ax = fig.gca()
ax.add_artist((plt.Circle((0, 0), 0.9)) """
plt.grid(True, which="both")
plt.xlabel(r'$\mathbf{Inphase}$')
plt.ylabel(r'$\mathbf{Quadrature}$')
plt.title(r'$\mathbf{Geometrically\:Shaped\:Constellation}$')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
# plt.show()
absFilePath = os.path.abspath(__file__)
os.chdir(os.path.dirname(absFilePath))
plt.savefig('GS1.eps')
