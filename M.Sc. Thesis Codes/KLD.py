
from numpy import log2, sum
import numpy as np
arr = np.array


def KLD(a, b):
    a = np.asarray(a, dtype=np.float)
    b = np.asarray(b, dtype=np.float)
    return np.sum(np.where(a != 0, a * np.log2(a / b), 0))

p1 = [1/16, 1/16, 1/16]
p2 = [0.4930/4, 0.3420/8, 0.1650/4]
p3 = [0.5285/4, 0.3360/8, 0.1355/4]
p4 = [0.6745/4, 0.2780/8, 0.0475/4]
y1 = KLD(p1,p2)
print(y1)
y2 = KLD(p1,p3)
print(y2)
y3 = KLD(p1,p4)
print(y3)
print()
print(max(y1,y2,y3))
#print(p1[0])

