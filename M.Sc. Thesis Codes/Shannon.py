# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:42:03 2020

@author: Ahmad
"""

from numpy import log2
import numpy as np
import matplotlib.pyplot as plt
arr = np.array

SR = {'P1': 1, 'P2': 0.9702, 'P3':0.9302, 'P4': 0.9002} #Shaping Rate of 16-QAM Distributions in Dictionary form

# SR = {'P1': 1, 'P2': 0.9503, 'P': 0.9003} #Shaping Rate of 64-QAM Distributions in Dictionary form

# SR = {'P1': 1, 'P2': 0.9506, 'P': 0.9005} #Shaping Rate of 256-QAM Distributions in Dictionary form

CR = {'1': 0.855, '2': 0.744, '3': 0.566, '4': 0.410, '5': 0.299, '6': 0.166} #Rate of the Codes

Rs = 32e9 #Baud Rate
# M = 8 #Modulation Order


# def entr(p1,p2,p3,p4):
#     return -p1*log2(p1/4)-p2*log2(p2/8)-p3*log2(p3/4)-p4*log2(p4/4);

def entr(p1,p2):
    return -p1*log2(p1/4)-p2*log2(p2/4)

P='P'
P1='P1'
P2='P2'
P3='P3'
P4='P4'
C1='1'
C2='2'
C3='3'
C4='4'
C5='5'
C6='6'

def BR(ent, M, code):
# def BR(ent, M):
     m = np.log2(M) #Number of bit-levels of Modulation, two 4-PAM (16-QAM=4-PAM * 4-PAM)
     # BPS = Ent[ent]-((1-CR[code])*m) #Bit per Symbol
     BPS = 2*m*CR[code]*SR[ent] 
     # return 2*BPS*Rs*1e-9
     return BPS/1.01
# print(BR(P1, C2))

EsN0_dB = list(np.arange(-10,26.1)) #SNR per Symbol 
EsN0_dB = arr(EsN0_dB)
EsN0 = 10**(0.1*EsN0_dB)
# C = 2*1.01*Rs*np.log2(1+snr) #Shannon Capacity Limit
SE = 2*np.log2(1+EsN0/1.01) #Shannon Spectral Eff. Limit (bit/s/Hz) for Dual Polarization
plt.plot(EsN0_dB, SE, 'k-', label='$\mathbf{Shannon\:\:Limit}$')
plt.xlabel('$\mathbf{SNR\:per\:Symbol\:[dB]}$')
# plt.ylabel('$\mathbf{Information\:Bit\:Rate\:R_{b}\:[Gbit/s]}$')
plt.ylabel('$\mathbf{Spectral\:Efficiency\:[bit/s/Hz]}$')
plt.grid(True, which='both')

# =============================================================================
# 4-ASK
# =============================================================================


# SNR = [5.1181]
# R = [BR(P1,4)]
# M1 = ['*']
# for i,j,m in zip(SNR,R,M1): 
#     plt.scatter(i, j, c='g', marker=m)
# plt.plot(SNR, R, 'g--', label='$\mathbf{Uniform\:4-ASK\:[P_{1}]}$')



# SNR=arr(SNR)
# SNR_Sh=SNR-2.47
# R = [BR(P4,4)]
# M1 = ['*']
# for i,j,m in zip(SNR_Sh,R,M1): 
#     plt.scatter(i, j, c='c', marker=m)
# plt.plot(SNR_Sh, R, 'c--', label='$\mathbf{Shaped\:\:4-ASK\:[P_{2}]}$')


# =============================================================================
# #8-QAM
# =============================================================================

# SNR = [2.2, 4.3, 5.9, 7.5, 9.5, 10.8] #8-QAM SNR Values
# R = [BR(P,8,C6), BR(P,8,C5), BR(P,8,C4), BR(P,8,C3), BR(P,8,C2), BR(P,8,C1)] #8-QAM Rate Values
# M1 = ['*', 'v', 'o', 's', '^', 'd']
# for i,j,m in zip(SNR,R,M1): 
#     plt.scatter(i, j, c='b', marker=m)
# plt.plot(SNR, R, 'b-', label='$\mathbf{Uniform\:8-QAM\:[P_{1}^{\'}]}$')


# SNR=arr(SNR)
# SNR_Sh=SNR-2.34
# R = [BR(PP,8,C6), BR(PP,8,C5), BR(PP,8,C4), BR(PP,8,C3), BR(PP,8,C2), BR(PP,8,C1)] #8-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh,R,M1): 
#     plt.scatter(i, j, c='lime', marker=m)
# plt.plot(SNR_Sh, R, 'lime', label='$\mathbf{Shaped\:\:8-QAM\:[P_{2}^{\'}]}$')


# SNR=arr(SNR)
# SNR_Sh=SNR-4.4399999999999995
# R = [BR(PPP,8,C6), BR(PPP,8,C5), BR(PPP,8,C4), BR(PPP,8,C3), BR(PPP,8,C2), BR(PPP,8,C1)] #8-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh,R,M1): 
#     plt.scatter(i, j, c='deeppink', marker=m)
# plt.plot(SNR_Sh, R, 'deeppink', label='$\mathbf{Shaped\:\:8-QAM\:[P_{*}^{\'}]}$')



# =============================================================================
# #16-QAM
# =============================================================================


SNR = [4.2, 6.1, 7.5, 9.7, 11.55, 13.1] #16-QAM SNR per Symbol Values
R = [BR(P1,16,C6), BR(P1,16,C5), BR(P1,16,C4), BR(P1,16,C3), BR(P1,16,C2), BR(P1,16,C1)] #16-QAM Rate Values
M1 = ['*', 'v', 'o', 's', '^', 'd']
# M1.pop(0)
for i,j,m in zip(SNR,R,M1): 
    plt.scatter(i, j, c='g', marker=m)
plt.plot(SNR, R, 'g--', label='$\mathbf{Uniform\:16-QAM\:[P_{1}]}$')
# plt.axhline(y=BR(P1,16,C6), c='g', xmin=0.32, xmax=0.55, ls='--')

SNR=arr(SNR)
SNR_Sh1=arr([3.8527259897500334, 5.5485611778548645, 6.827952740074469, 8.881271445695845, 10.64123999076437, 12.134474768437897])
R = [BR(P2,16,C6), BR(P2,16,C5), BR(P2,16,C4), BR(P2,16,C3), BR(P2,16,C2), BR(P2,16,C1)] #16-QAM Shaped Rate Values
for i,j,m in zip(SNR_Sh1,R,M1): 
    plt.scatter(i, j, c='b', marker=m)
plt.plot(SNR_Sh1, R, 'b--', label='$\mathbf{Shaped\:\:16-QAM\:[P_{2}]}$')
# plt.axhline(y=BR(P2,16,C6), c='b',xmin=0.29, xmax=0.5, ls='--')

SNR=arr(SNR)
SNR_Sh2=arr([3.4758915379230526, 5.087370891672132, 6.315349946431745, 8.304412638431153, 10.02391575678083, 11.491197551385707])
R = [BR(P3,16,C6), BR(P3,16,C5), BR(P3,16,C4), BR(P3,16,C3), BR(P3,16,C2), BR(P3,16,C1)] #16-QAM Shaped Rate Values
for i,j,m in zip(SNR_Sh2,R,M1): 
    plt.scatter(i, j, c='r', marker=m)
plt.plot(SNR_Sh2, R, 'r--', label='$\mathbf{Shaped\:\:16-QAM\:[P_{3}]}$')
# # plt.axhline(y=BR(P3,16,C6), c='r',xmin=0.26, xmax=0.46, ls='--')

SNR=arr(SNR)
SNR_Sh3=arr([3.197709403414957, 4.767484881878317, 5.969690493131033, 7.926136050885408, 9.62485102728319, 11.078691675086944])
R = [BR(P4,16,C6), BR(P4,16,C5), BR(P4,16,C4), BR(P4,16,C3), BR(P4,16,C2), BR(P4,16,C1)] #16-QAM Shaped Rate Values
for i,j,m in zip(SNR_Sh3,R,M1): 
    plt.scatter(i, j, c='y', marker=m)
plt.plot(SNR_Sh3, R, 'y--', label='$\mathbf{Shaped\:\:16-QAM\:[P_{4}]}$')
# # plt.axhline(y=BR(P4,16,C6), c='y',xmin=0.25, xmax=0.41, ls='--')

print(SNR-SNR_Sh3)
# SNR=arr(SNR)
# SNR_Sh=SNR-1.75
# R = [BR(P,16,C6), BR(P,16,C5), BR(P,16,C4), BR(P,16,C3), BR(P,16,C2), BR(P,16,C1)] #16-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh,R,M1): 
#     plt.scatter(i, j, c='c', marker=m)
# plt.plot(SNR_Sh, R, 'c--', label='$\mathbf{Shaped\:\:16-QAM\:[P_{*}]}$')

# plt.text()


# SNR = [4.2, 6.1, 7.5, 9.7, 11.55, 13.1] #16-QAM SNR Values
# R = [BR(P1,16,C6), BR(P1,16,C5), BR(P1,16,C4), BR(P1,16,C3), BR(P1,16,C2), BR(P1,16,C1)] #16-QAM Rate Values
# M1 = ['*', 'v', 'o', 's', '^', 'd']
# # M1.pop(0)
# for i,j,m in zip(SNR,R,M1): 
#     plt.scatter(i, j, c='g', marker=m)
# plt.plot(SNR, R, 'g--', label='$\mathbf{Uniform\:16-QAM\:[P_{1}]}$')


# SNR=arr(SNR)
# SNR_Sh1=SNR-0.68
# R = [BR(P2,16,C6), BR(P2,16,C5), BR(P2,16,C4), BR(P2,16,C3), BR(P2,16,C2), BR(P2,16,C1)] #16-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh1,R,M1): 
#     plt.scatter(i, j, c='b', marker=m)
# plt.plot(SNR_Sh1, R, 'b--', label='$16-QAM\:[Shaped:P_{2}]$')

# SNR=arr(SNR)
# SNR_Sh2=SNR-0.91
# R = [BR(P3,16,C6), BR(P3,16,C5), BR(P3,16,C4), BR(P3,16,C3), BR(P3,16,C2), BR(P3,16,C1)] #16-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh2,R,M1): 
#     plt.scatter(i, j, c='r', marker=m)
# plt.plot(SNR_Sh2, R, 'r--', label='$16-QAM\:[Shaped:P_{3}]$')


# SNR=arr(SNR)
# SNR_Sh3=SNR-2.01
# R = [BR(P4,16,C6), BR(P4,16,C5), BR(P4,16,C4), BR(P4,16,C3), BR(P4,16,C2), BR(P4,16,C1)] #16-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh3,R,M1): 
#     plt.scatter(i, j, c='m', marker=m)
# plt.plot(SNR_Sh3, R, 'm--', label='$\mathbf{Shaped\:\:16-QAM\:[P_{4}]}$')

 

# =============================================================================
# #64-QAM
# =============================================================================
           
# SNR=[11.699173314575678, 13.27571629284304, 14.48212056204019, 16.443898393754182, 18.146023372240027, 19.602073942267065]#64-QAM SNR Values
# R = [BR(P1,64,C6), BR(P1,64,C5), BR(P1,64,C4), BR(P1,64,C3), BR(P1,64,C2), BR(P1,64,C1)] #64-QAM Rate Values
# M1 = ['*', 'v', 'o', 's', '^', 'd']
# # M1.pop(0)
# for i,j,m in zip(SNR,R,M1): 
#     plt.scatter(i, j, c='b', marker=m)
# plt.plot(SNR, R, 'b--', label='$\mathbf{Uniform\:64-QAM\;[P_{1}^{\'\'}]}$')

# SNR=arr(SNR)
# SNR_Sh=[10.225619813067299, 11.669519141394042, 12.792453735663461, 14.64682550378394, 16.279377244487925, 17.689938527057013]
# R = [BR(P2,64,C6), BR(P2,64,C5), BR(P2,64,C4), BR(P2,64,C3), BR(P2,64,C2), BR(P2,64,C1)] #64-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh,R,M1): 
#     plt.scatter(i, j, c='y', marker=m)
# plt.plot(SNR_Sh, R, 'y--', label='$\mathbf{Shaped\:\:64-QAM\:[P_{2}^{\'\'}]}$')

# SNR=arr(SNR)
# SNR_Sh1=[9.278017713802127, 10.687995014448111, 11.78917648744872, 13.615061865810116, 15.228842122247439, 16.626983599922013]
# R = [BR(P,64,C6), BR(P,64,C5), BR(P,64,C4), BR(P,64,C3), BR(P,64,C2), BR(P,64,C1)] #64-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh1,R,M1): 
#     plt.scatter(i, j, c='r', marker=m)
# plt.plot(SNR_Sh1, R, 'r--', label='$\mathbf{Shaped\:\:64-QAM\:[P_{*}^{\'\'}]}$')


# =============================================================================
# #256-QAM
# =============================================================================
           
# SNR=[18.261069302221493, 19.724180946349065, 20.859361132002196, 22.729677392142445, 24.372676769902778, 25.79012333835689] #256-QAM SNR Values
# R = [BR(P1,256,C6), BR(P1,256,C5), BR(P1,256,C4), BR(P1,256,C3), BR(P1,256,C2), BR(P1,256,C1)] #256-QAM Rate Values
# M1 = ['*', 'v', 'o', 's', '^', 'd']
# # M1.pop(0)
# for i,j,m in zip(SNR,R,M1): 
#     plt.scatter(i, j, c='b', marker=m)
# plt.plot(SNR, R, 'b--', label='$\mathbf{Uniform\:256-QAM\;[P_{1}^{\'\'}]}$')

# SNR=arr(SNR)
# SNR_Sh=[16.1133025634809875, 17.506592579377415, 18.597008140812033, 20.408717509218054, 22.013105316354107, 23.40500873851593]
# R = [BR(P2,256,C6), BR(P2,256,C5), BR(P2,256,C4), BR(P2,256,C3), BR(P2,256,C2), BR(P2,256,C1)] #256-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh,R,M1): 
#     plt.scatter(i, j, c='y', marker=m)
# plt.plot(SNR_Sh, R, 'y--', label='$\mathbf{Shaped\:\:256-QAM\:[P_{2}^{\'\'}]}$')

# SNR=arr(SNR)
# SNR_Sh1=[14.797539678215902, 16.176635893854534, 17.257866180828035, 19.057439777991274, 20.65375977742424, 22.040292210851582]
# R = [BR(P,256,C6), BR(P,256,C5), BR(P,256,C4), BR(P,256,C3), BR(P,256,C2), BR(P,256,C1)] #256-QAM Shaped Rate Values
# for i,j,m in zip(SNR_Sh1,R,M1): 
#     plt.scatter(i, j, c='r', marker=m)
# plt.plot(SNR_Sh1, R, 'r--', label='$\mathbf{Shaped\:\:256-QAM\:[P_{*}^{\'\'}]}$')


plt.legend()


# SNR = [7.995102357693452, 8.693425648368581, 8.926206067730428, 10.031752248985907]
# SNR = [10.743455682160155, 11.474598979984345, 11.711504043595685, 12.830121498643816]
# SNR = [9.701291988830022, 7.7723875816142325, 7.372216934135349, 5.714400630266691]
# R=[]
# Ent={'P1': 4, 'P2': 3.8033, 'P3': 3.7417, 'P4':3.3834}
# P1='P1'
# P2='P2'
# P3='P3'
# P4='P4'
# for x in Ent:
#     print(Ent[x])
#     R.append(2*Rs*(1e-9)*Ent[x])  
# plt.scatter(SNR, R)

# plt.savefig('Shannon16.eps')
plt.show()