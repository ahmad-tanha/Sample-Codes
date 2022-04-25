"""
Created on Mon Aug 26 11:23:57 2019

@author: Ahmad
"""

from math import sqrt
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
# import komm as k
arr=np.array

# f = open('W4_256.txt', 'r')
f = open('a4_256.txt', 'r')
D4 = []
for x in f:
    #print(x)
    D4.append(x.rstrip('\n')) #removing \n from end of each line via rstrip command
D4=[[float(i) for i in row.split()] for row in D4]
# print(D4)
f.close()
x = D4    
# M = 16
# qam = k.QAModulation(M)
#qam=k.QAModulation(orders=(4, 2), base_amplitudes=(1.0, 2.0))
# x=list(qam.constellation)
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
def prob(x,p):
    num_ev = 0
    for i in range(1000):  # set up simulation for 1000 coin tosses
        if rnd.random() < p1:  # toss coin with probability p
            x[i] = 1  # The first event is happening
        elif rnd.random() < p2:
                        # The second event is happening
        elif rnd.random() < p3:

        n += num_ev  # count number of event occurances
"""
sorted_const = []
M = len(x)
d = np.zeros(len(x))
for i in range(len(x)):
    for j in range(len(x[i])):
        d[i] = d[i] + round(x[i][j]**2,2)
d = list(d)
# print(d)
d2 = list(set(d))
d2.sort()
print('d2 sorted values are:\n', d2)
num_prob = 0 #number of probabilities
for i in range(len(d2)): 
    q = d.index(d2[i])
    # print(q)
    w = d.count(d2[i])
    print('\nnumber of', d2[i],'\'s is', w)
    n = 1
    Q = []
    while n<w: 
        Q.append(q)
        q = d.index(d2[i],q+1,M)
        n+=1
        # print(x[q])       
    Q.append(q)
    print('corresponding indexes are:\n',Q)
    Q=arr(Q)
    # print(x[Q])
    const=[]
    for t in range(len(Q)):
        const.append(x[Q[t]])
    print('\ncorresponding constellation points are:\n',const)
    # print('\nindexes of d2 =',d2[i], 'are:\n', Q)    
    sorted_const.append(const)
    num_prob += 1
print('\nnumber of shells is:', num_prob)
print('\nsorted_const:\n',sorted_const)



u=[1,0,0,0]
# u=[0,1,1,1]
neigh=[]
for i in range(256):
    ED2=(u[0]-x[i][0])**2+(u[1]-x[i][1])**2+(u[2]-x[i][2])**2+(u[3]-x[i][3])**2
    if ED2==2:
        # print(i)
        neigh.append(x[i])    
print('\n\n\n',neigh,'\n\n\n')
print('nearest neighbours (X)',' :','norm2(u)-norm2(X)',',  ','u-X')

def norm2(x):
    return x[0]**2+x[1]**2+x[2]**2+x[3]**2

def dist(u,x):
    d=[]
    for i in range(4):
        d.append(u[i]-x[i])
    return d

for X in neigh:
    print(X,' : ',norm2(u)-norm2(X),' ,   ',dist(u,X))

  

"""    
xp1 = list({x[int((M/2-1)-(m.sqrt(M)/2))], x[int((M/2-1)-(m.sqrt(M)/2)+1)]})
print("xp1 is:", xp1)
print(x[int((M/2-1)-(m.sqrt(M)/2)+m.sqrt(M)):int((M/2-1)-(m.sqrt(M)/2)+2+m.sqrt(M))])
print(x[int((M/2-1)-(m.sqrt(M)/2)+m.sqrt(M)):int((M/2-1)-(m.sqrt(M)/2)+2+m.sqrt(M))])
"""
#ent = k.entropy([0.2,0.15,0.145,0.102,0.106,0.113,0.0115,0.0107,0.0103])
#print(ent)

# plt.hist(list(range(5)),bins=50)
# plt.plot(list(range(5)),np.histogram(d2))
