# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 00:01:14 2020

@author: Ahmad
"""

import numpy as np
from numpy import log2
from scipy.stats import entropy as ent
# from collections import Counter

N = 4 # Number of dimensions (Shell Mapper's Output Length)

"""for a4_256"""
# M = 32 #Number of rings (Shell Mapper's Output Alphabet)
# K = 16 #Number of input bits (Shell Mapper's Input Length)

"""for PM-16QAM"""
M = 16 
K = 12

"""for 16QAM """
# M = 4
# K = 6

g = np.zeros([int(log2(N)),N*(M-1)+1]) #g[2^{1 ... log2(N)}][0-N*(M-1)]  This is for computing M_p(j)
zN = np.zeros(N*(M-1)+1) #This is for computing C_N(j)

#First we compute g2
for p in range(2*(M-1)+1):
    g[0, p] = M - abs(p - M +1)
    
#Then we proceed with g4, g8, ..., and g(N)
for k in range(1,int(log2(N))):
    for p in range(N*(M-1)+1):  
        g[k, p] = 0
        zN[p] = 0
        for i in range(p+1):
            g[k, p] = g[k, p] + g[k-1,i]*g[k-1,p-i] 
            zN[p] = zN[p] + g[int(log2(N)-1), i]
        if 2**K <= zN[p]:
            thr = p
            zN[p] = 0
            g[k, p] = 0
            break


def Shell_mapper_enc(Idx):
    W  = np.zeros([int(log2(N)),2**(int(log2(N)-1))]) #this vector represents the wieghts of subvectors for log2(N) steps  >>>>> omega_{N, N/2}
    R = np.zeros([int(log2(N)),2**(int(log2(N)-1))]) #R is the index in each step  >>>>> D_N(V^[N])
    RR = np.zeros([int(log2(N)),2**(int(log2(N)-1))]) #RR is the offset index  >>>>> N_N(V^[N]), d
    Ring_Index = np.zeros(N)  # the final ring index which is the encoder's output
    
    # Idx=7
    R[int(log2(N)-1),0] = Idx
    #Here we find weight of V^[N]
    for p in range(thr):
        if zN[p] <= R[int(log2(N))-1,0]:
            W[int(log2(N)-1),0] = p+1
    
    """Then we move using 8.60 and 8.66 and 8.67
     	  take a look at V.34 shell mapping algorithm given in the standard
     	  The implementation has been inspired significantly by V.34 standard"""
    for k in range(int(log2(N)-1),0,-1):
        for p in range(2**(int(log2(N)-k-1))): 
            if k == int(log2(N)-1):
                RR[k,p]= R[k,p]- zN[int(W[int(log2(N)-1),0]-1)]		
            else:
                RR[k,p] = R[k,p]
                
            W[k-1,2*p] = -1
            
            while RR[k,p] >= 0:
                W[k-1,2*p] += 1
                # print(W[k-1,2*p])
                W[k-1,2*p+1] = W[k,p] - W[k-1,2*p]
                RR[k,p]  -= g[k-1,int(W[k-1,2*p])]*g[k-1,int(W[k-1,2*p+1])]
            
            RR[k,p] += g[k-1,int(W[k-1,2*p])]*g[k-1,int(W[k-1,2*p+1])]
    
            R[k-1,2*p+1] = RR[k,p] % g[k-1,int(W[k-1,2*p+1])]    # there is diffrence in V.34 standard, so the code is based on Tretter's book
            R[k-1,2*p] = (RR[k,p] - R[k-1,2*p+1])/g[k-1,int(W[k-1,2*p+1])] # there is diffrence in V.34 standard % there is diffrence in V.34 standard
    		    
    """ The last step is to get from the weight and the index of pairs (2 dimensional vectors) to 1D dimensional indexes
    	 See 8.68 and 8.69 of tretter's book Chap. 8 """
    for p in range(2**(int(log2(N)-1))):
        if W[0,p] <= M-1:	
            Ring_Index[2*p] = np.rint(R[0,p]) 
            Ring_Index[2*p+1] = np.rint(W[0,p]-Ring_Index[2*p]) 	 
        else:	
            Ring_Index[2*p] = np.rint(W[0,p] + R[0,p] - (M-1)) 
            Ring_Index[2*p+1] = np.rint(W[0,p]-Ring_Index[2*p]) 	 
        
    return Ring_Index 
                  

count = np.zeros(M)
pmf = np.zeros(M)
for idx in range(2**K):
    print(idx, ':', Shell_mapper_enc(idx))
    for x in Shell_mapper_enc(idx):
        # print(x)
        for i in range(M):
            if x == i:
                count[i] +=1
pmf = list(count/sum(count))                


"""for a4_256"""
# PMF_a4=np.kron(pmf,[1/8]*8)
# ENT=ent(PMF_a4, base=2)
# print('\n',ENT)



"""for PM-16QAM"""
PMF_PM16=np.kron(pmf,[1/16]*16)
ENT=ent(PMF_PM16, base=2)
print('\n',ENT)



# """for 16QAM"""
# PMF_16=np.kron(pmf,[1/4]*4)
# ENT=ent(PMF_16, base=2)
# print('\n',ENT)

# PMF_PM16=[]
# for i in range(16):
#     for j in range(16):
#         PMF_PM16.append(PMF_16[i]*PMF_16[j])
# PMF_PM16=np.sort(PMF_PM16)[::-1] #Reverse Sort       
# PMF_PM16=list(PMF_PM16)  
# print('\n', PMF_PM16)
# ENT=ent(PMF_PM16, base=2)
# print('\n',ENT)

# #M_p(j)
# for k in range(1,int(log2(N))+1):
#     p=2**k
#     for i in range(p+1):
#         g[k, p] = g[k, p] + g[k-1,i]*g[k-1,p-i]
#     		# zN[p] = zN[p] + g[int(log2(k)-1), i]
#    	# zN[p] = zN[p] - g[int(log2(k)-1), p]


# """This function computes M_p(j) or number of p-tuples with weight j"""
# def wei(p,j):
#     if p==1:
#         if j<M:
#             return 1
#         else: 
#             return 0
#     x=0
#     for k in range(j+1):
#        x += wei(p/2,k)*wei(p/2,j-k)
#        # print(x)
#     return x 
  
# print(wei(2,4))

# """Here we compute C_N(j) or number of N-tuples with weight j and threshold J""" 
# thr=[] #threshold
# wei_thr=0 #C_N(j)
# # zN=[]
# for k in range(N*(M-1)+1):
#     wei_thr += wei(N,k)  
#     if (2**K) <= wei_thr:
#         # print(k)
#         # print(wei_thr)
#         thr.append(k)       
#     # else:
#         # zN.append(wei_thr)
# thr = min(thr)
# print(thr)


# """Storing M_p(j) for future use"""
# g=[] 
# for k in range(int(log2(N))+1):
#     gg=[] #list of same p-tuple of different weights
#     p = 2**k
#     if p == 1:
#         for j in range(M):
#             gg.append(wei(p,j))
#         g.append(gg) 
#     else:
#         for j in range(thr):
#             # print(wei(p,j))
#             gg.append(wei(p,j))
#         g.append(gg)        





        

    
    
    
        
