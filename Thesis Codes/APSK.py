
from numpy import pi, exp, log, sqrt, concatenate, sum, real, imag
from numpy import array as arr
import matplotlib.pyplot as plt
import numpy as np
import os

teta_in=[]
teta_out=[]
for i in range(8):
    teta_in.append(pi/8+i*pi/4)
    teta_out.append(pi/8+i*pi/4)
# print(teta)    
# print(log(exp(1)))
# r1 = sqrt(log(8/7))
# Pdbm=0.5
# m=0.6302
m=0.5
# r1=sqrt((10**((Pdbm-30)/10))*(m**2)/(m**2+1))
r1 = 0.5
#print(r1)
# r2 = sqrt(log(8/5))
r2 = r1/m
#print(r2)
teta_in=arr(teta_in)
teta_out=arr(teta_out)
x1=(r1*exp(1j*teta_in))
x2=(r2*exp(1j*teta_out))
x=concatenate([x1,x2])
# print(x)
# power=(r1**2+r2**2)/2
# print(abs(x))
# print(sum(x))
# plt.plot(real(x1), imag(x1),'c-')
# plt.plot(real(x2), imag(x2),'c-')
circle1=plt.Circle((0, 0), r1, color='b', linestyle='--', fill=False)
circle2=plt.Circle((0, 0), r2, color='b', linestyle='--', fill=False)
ax = plt.gca()
# xx1 = [0, np.real(x1[0]), np.real(x2[0])]
# yy1 = [0, np.imag(x1[0]), np.imag(x2[0])]
# xx2 = [0, np.real(x1[1]), np.real(x2[1])]
# yy2 = [0, np.imag(x1[1]), np.imag(x2[1])]
# # Find the slope and intercept of the best fit line
# slope1, intercept1 = np.polyfit(xx1, yy1, 1)
# slope2, intercept2 = np.polyfit(xx2, yy2, 1)

for i in range(8):
    xx=([0, np.real(x1[i]), np.real(x2[i])])
    yy=([0, np.imag(x1[i]), np.imag(x2[i])])
    slope, intercept = np.polyfit(xx, yy, 1)
    abline_values = [slope * ii + intercept for ii in xx]
    plt.plot(xx, abline_values, 'b', linestyle='--')
    hold = 'True'

# # Create a list of values in the best fit line
# abline_values1 = [slope1 * i + intercept1 for i in xx1]
# abline_values2 = [slope2 * i + intercept2 for i in xx2]

# plt.plot(xx1, abline_values1, 'b', linestyle='--')
# plt.plot(xx2, abline_values2, 'b', linestyle='--')
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
# plt.xlim(-0.8, 0.8)
# plt.ylim(-0.8, 0.8)
# plt.show()
absFilePath = os.path.abspath(__file__)
os.chdir(os.path.dirname(absFilePath))
plt.savefig('GS3.eps')

p = [1/16, 1/16, 1/16] #P1 Uniform, Entropy = 4, Shaping Rate = 1
npx = np.real(x)
npy = np.imag(x)
d2 = npx**2+npy**2
#print(d2)
d4 = d2**2
#print(d4)
d6 = d2**3
# print(d6)
exd2 = p[0]*sum(d2[0:4])+p[1]*sum(d2[4:12])+p[2]*sum(d2[12:16])
print('exd2 =', exd2)
exd4 = p[0]*sum(d4[0:4])+p[1]*sum(d4[4:12])+p[2]*sum(d4[12:16])
print("exd4 =", exd4)
exd6 = p[0]*sum(d6[0:4])+p[1]*sum(d6[4:12])+p[2]*sum(d6[12:16])
print("exd6 =", exd6)
kurr = (exd4/(exd2**2))
print("kurr =", kurr)
kurr3 = (exd6/(exd2**3))
print("kurr3 =", kurr3)
# phi = kurr-2
# print("phi =", phi)
# si = kurr3-9*kurr+12
# print("si =", si)
