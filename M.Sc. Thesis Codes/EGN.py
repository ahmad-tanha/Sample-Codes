
# =============================================================================
# =============================================================================
# #     My EGN
# =============================================================================
# =============================================================================
    
    # -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 07:12:09 2020

@author: Ahmad
"""
import os
import numpy as np
from numpy import pi, exp, sin, conj, random
#import matplotlib
#matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
arr=np.array

#System parameters
gamma = 1.3e-3       #Nonlinearity coefficient in [1/W/km]
beta2 = -1.9378e-26     #Dispersion coefficient[ps ^ 2/km]
alpha = 0.22          #Fiber loss coefficient[dB/km]
alpha_norm = (alpha*1e-3)/4.343
Nspan = 50           #Number of spans
L = 140e3             #Span length[km]
#PdBm = 2            #Average input power[dBm]
R = 32.5e9             #Baud-rate[GHz]
CS = 1.05*R  # Channel spacing[GHz] #f_CUT = 0
f_int1 = -CS  # First Interfering Channel
f_int2 = CS  # Second Interfering Channel
# Second order modulation factor < |a | ^4 > / < |a | ^2 > ^2
kur = [1.32, 1.6474842486154304, 1.693786770762844,
       1.847323956725728, 1.4014259087800531]
# Third order modulation factor < |a | ^6 > / < |a | ^2 > ^3
kur3 = [1.96, 3.260013421565045, 3.5078766205404968,
        4.526644880652631, 2.1273420495164355]
#N = 1000000    #Number of integration points in algorithm[14]. Should be set such that the relative error is desirably small.



_N=250000                # Monte Carlo Mesh Grid
def zeta(f1,f2,f):
    temp = alpha_norm-4j*pi**2*beta2*(f1-f)*(f2-f)
    temp=gamma*(1-exp(-temp*L))/temp
    return temp

def nu(f1,f2,f):
    temp=2*pi**2*beta2*(f1-f)*(f2-f)*L
    temp = sin(Nspan*temp)/sin(temp)*exp(1j*(Nspan-1)*temp)
    return temp

def mu(f1,f2,f):
    return nu(f1,f2,f)*zeta(f1,f2,f)

def pulseshape(f, f_int=0,pulseshape='rect'):
    '''
    Pulse Shape; for now, it is assumed to be
    rectangular in frequency
    '''
    if pulseshape=='rect':
        return (f-f_int<R/2)*(f-f_int>-R/2)/R
    else:
        return 0
    return

def _2DMC(f,x0,x1,y0,y1):
    '''
    2D Monte Carlo Integration
    '''
#    _N=100000
    random.seed(0)
    x=random.uniform(x0,x1,_N)
    y=random.uniform(y0,y1,_N)
    result=(x1-x0)*(y1-y0)*sum(f(x,y))/_N
    return result

def _3DMC(f, x0, x1, y0, y1, z0, z1):
    '''
    3D Monte Carlo Integration
    '''
#    _N = 100000
    random.seed(0)
    x = random.uniform(x0, x1, _N)
    y = random.uniform(y0, y1, _N)
    z = random.uniform(z0, z1, _N)
    result = (x1-x0)*(y1-y0)*(z1-z0)*sum(f(x, y, z))/_N
    return result

def _4DMC(f, x0, x1, y0, y1, z0, z1, w0, w1):
    '''
    4D Monte Carlo Integration
    '''
#    _N = 100000
    random.seed(0)
    x = random.uniform(x0, x1, _N)
    y = random.uniform(y0, y1, _N)
    z = random.uniform(z0, z1, _N)
    w = random.uniform(w0, w1, _N)
    result = (x1-x0)*(y1-y0)*(z1-z0)*(w1-w0)*sum(f(x, y, z, w))/_N
    return result


def _5DMC(f, x0, x1, y0, y1, z0, z1, w0, w1, q0, q1):
    '''
    5D Monte Carlo Integration
    '''
#    _N = 100000
    random.seed(0)
    x = random.uniform(x0, x1, _N)
    y = random.uniform(y0, y1, _N)
    z = random.uniform(z0, z1, _N)
    w = random.uniform(w0, w1, _N)
    q = random.uniform(q0, q1, _N)
    result = (x1-x0)*(y1-y0)*(z1-z0)*(w1-w0)*(q1-q0)*sum(f(x, y, z, w, q))/_N
    return result

G = exp(alpha_norm*L)
def zigma2_ASE(Nspan,G,NF,lamda,beta,Rs):
    h = 6.626*(1e-34)
    c = 3*(1e8)
    return 0.5*Nspan*G*(10**(0.1*NF))*h*c*(1+beta)*Rs/(lamda*(1e-9))

ASE = zigma2_ASE(Nspan, G, 5.5, 1550,0.01,R)

#L_list=np.linspace(1,1000,1000)
"""
k1  = []
k2  = []
k3  = []
k11 = []
k12 = []
"""
    
kappa1 = (16/27)*(R**3)*_3DMC(lambda f1, f2, f: (pulseshape(f1)**2)*(pulseshape(f2)**2)*(pulseshape(f1+f2-f)**2)*\
            (abs(mu(f1, f2, f))**2), -R/2, R/2, -R/2, R/2, -R/2, R/2)
#print(kappa1)

kappa2 = (80/81)*(R**2)*_4DMC(lambda f1, f2, f2p, f: (pulseshape(f1)**2)*pulseshape(f2)*conj(pulseshape(f2p))*conj(pulseshape(f1+f2-f))*\
    pulseshape(f1+f2p-f)*mu(f1, f2, f)*conj(mu(f1, f2p, f)), -R/2, R/2, -R/2, R/2, -R/2, R/2, -R/2, R/2)+\
    (16/81)*(R**2)*_4DMC(lambda f1, f2, f2p, f: (pulseshape(f1+f2-f)**2)*pulseshape(f1) * pulseshape(f2) *\
                        conj(pulseshape(f1+f2-f2p))*conj(pulseshape(f2p))*mu(f1, f2, f) *conj(mu(f1+f2-f2p,f2p,f))\
                            , -R/2, R/2, -R/2, R/2, -R/2, R/2, -R/2, R/2)
#print(kappa2)

kappa3 = (16/81)*R*_5DMC(lambda f1, f2, f1p, f2p, f: pulseshape(f1)*pulseshape(f2)*conj(pulseshape(f1+f2-f))*\
                        conj(pulseshape(f1p))*conj(pulseshape(f2p))*pulseshape(f1p+f2p-f)*mu(f1,f2,f)*conj(mu(f1p,f2p,f)),\
                        -R/2, R/2, -R/2, R/2, -R/2, R/2, -R/2, R/2, -R/2, R/2)
#print(kappa3)                         

kappa11 = (32/27)*(R**3)*(_3DMC(lambda f1, f2, f: (abs(pulseshape(f1))** 2)*(abs(pulseshape(f2, f_int1))**2)*(abs(pulseshape(f1+f2-f, f_int1))**2)*\
    abs(mu(f1, f2, f)**2),-R/2, R/2, f_int1-R/2, f_int1+R/2, -R/2, R/2)+_3DMC(lambda f1, f2, f: (abs(pulseshape(f1))** 2)*(abs(pulseshape(f2, f_int2))**2)*(abs(pulseshape(f1+f2-f, f_int2))**2)*\
    abs(mu(f1, f2, f)**2),-R/2, R/2, f_int2-R/2, f_int2+R/2, -R/2, R/2))
#print(kappa11)

kappa12 = (80/81)*(R**2)*(_4DMC(lambda f1, f2, f2p, f: (abs(pulseshape(f1)) ** 2)*pulseshape(f2, f_int1)*conj(pulseshape(f2p, f_int1))*conj(pulseshape(f1+f2-f, f_int1))*\
                            pulseshape(f1+f2p-f, f_int1)*mu(f1, f2, f)*conj(mu(f1, f2p, f)), -R/2, R/2, f_int1-R/2, f_int1+R/2, f_int1-R/2, f_int1+R/2, -R/2, R/2)+\
_4DMC(lambda f1, f2, f2p, f: (abs(pulseshape(f1)) ** 2)*pulseshape(f2, f_int2)*conj(pulseshape(f2p, f_int2))*conj(pulseshape(f1+f2-f, f_int2))*\
                            pulseshape(f1+f2p-f, f_int2)*mu(f1, f2, f)*conj(mu(f1, f2p, f)), -R/2, R/2, f_int2-R/2, f_int2+R/2, f_int2-R/2, f_int2+R/2, -R/2, R/2))
#print(kappa12)
"""
k1.append(kappa1)
k2.append(kappa2)
k3.append(kappa3)
k11.append(kappa11)
k12.append(kappa12)
#    k2[L] = kappa2
#    k3[L] = kappa3
#    k11[L] = kappa11
#    k12[L] = kappa12
#print(k1)
"""
"""
k1=arr(k1)
k2=arr(k2)
k3=arr(k3)
k11=arr(k11)
k12=arr(k12)
"""
# Pdbm = list(np.arange(-5,11,0.1))
Pdbm = np.linspace(-5,10,16)
P = np.zeros(len(Pdbm))
count = 0
for ind in Pdbm:
    P[count] = 10**((ind-30)/10)
    count = count+1

#NLIN Unshaped
NLIN_var_SCI = kappa1+((kur[0]-2)*kappa2)+((kur3[0]-9*kur[0]+12)*kappa3)
NLIN_var_XPM = kappa11+((kur[0]-2)*kappa12)
# NLIN_var_XPM = 0
NLIN = NLIN_var_XPM+NLIN_var_SCI
NV = abs((P**3)*NLIN) #Noise Variance
SNR = P/(NV+ASE)
SNR = 10*np.log10(SNR) 
# d=2*np.sqrt(P/10)
# Es=(5/2)*(d**2) #Energy per Symbol
# SNR_Sym=10*np.log10(Es/2/NV)
#print(NV)   
plt.plot(Pdbm, SNR, label=r"$\mathbf{me}$")

# #NLIN Shaped[1]
# NLIN_Sh1_var_SCI = kappa1+((kur[1]-2)*kappa2)+((kur3[1]-9*kur[1]+12)*kappa3)
# NLIN_Sh1_var_XPM = kappa11+((kur[1]-2)*kappa12)
# NLIN_Sh1 = NLIN_Sh1_var_XPM+NLIN_Sh1_var_SCI
# NV_Sh1 = abs((P**3)*NLIN_Sh1)  #Shaped Noise Variance
# SNR_Sh1 = P/(NV_Sh1+ASE)
# SNR_Sh1 = 10*np.log10(SNR_Sh1) 
# plt.plot(Pdbm, SNR_Sh1, label=r"$\mathbf{PS\:16-QAM\,[P_{2}]}$")

# #NLIN Shaped[2]
# NLIN_Sh2_var_SCI = kappa1+((kur[2]-2)*kappa2)+((kur3[2]-9*kur[2]+12)*kappa3)
# NLIN_Sh2_var_XPM = kappa11+((kur[2]-2)*kappa12)
# NLIN_Sh2 = NLIN_Sh2_var_XPM+NLIN_Sh2_var_SCI
# NV_Sh2 = abs((P**3)*NLIN_Sh2)  #Shaped Noise Variance
# SNR_Sh2 = P/(NV_Sh2+ASE)
# SNR_Sh2 = 10*np.log10(SNR_Sh2) 
# plt.plot(Pdbm, SNR_Sh2, label=r"$\mathbf{PS\:16-QAM\,[P_{3}]}$")

# #NLIN Shaped[3]
# NLIN_Sh3_var_SCI = kappa1+((kur[3]-2)*kappa2)+((kur3[3]-9*kur[3]+12)*kappa3)
# NLIN_Sh3_var_XPM = kappa11+((kur[3]-2)*kappa12)
# NLIN_Sh3 = NLIN_Sh3_var_XPM+NLIN_Sh3_var_SCI
# NV_Sh3 = abs((P**3)*NLIN_Sh3)  #Shaped Noise Variance
# SNR_Sh3 = P/(NV_Sh3+ASE)
# SNR_Sh3 = 10*np.log10(SNR_Sh3) 
# plt.plot(Pdbm, SNR_Sh3, label=r"$\mathbf{PS\:16-QAM\,[P_{4}]}$")

# #NLIN Shaped[4]
# NLIN_Sh4_var_SCI = kappa1+((kur[4]-2)*kappa2)+((kur3[4]-9*kur[4]+12)*kappa3)
# NLIN_Sh4_var_XPM = kappa11+((kur[4]-2)*kappa12)
# NLIN_Sh4 = NLIN_Sh4_var_XPM+NLIN_Sh4_var_SCI
# NV_Sh4 = abs((P**3)*NLIN_Sh4)  # Shaped Noise Variance
# SNR_Sh4 = P/(NV_Sh4+ASE)
# SNR_Sh4 = 10*np.log10(SNR_Sh4)
# plt.plot(Pdbm, SNR_Sh4, label=r"$\mathbf{GS\:16-QAM}$")

plt.xlabel(r"$\mathbf{Input\:Power\:[dbm]}$")
plt.ylabel(r"$\mathbf{SNR\:[dB]}$")
plt.title(r"$\mathbf{SNR\:Vs.\:Power}$")
plt.legend()
plt.grid(True, which="both")
plt.xlim(-5,10)
#plt.ylim(9, 10)
plt.show()
absFilePath = os.path.abspath(__file__)
os.chdir(os.path.dirname(absFilePath))
#plt.savefig('Power.eps')



