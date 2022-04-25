# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:14:41 2021

@author: Ahmad
"""

from math import sqrt
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
# import komm as k
arr=np.array
# import itertools

# f = open('W4_256.txt', 'r')
f = open('a2_4D.txt', 'r')

D4 = []
for x in f:
    #print(x)
    D4.append(x.rstrip('\n')) #removing \n from end of each line via rstrip command
D4=[[float(i) for i in row.split()] for row in D4]
# print(D4)
f.close()
x = D4    

X=[]
for i in range(0,256,16):
    X.append(complex(x[i][0],x[i][1]))

X[15]=2+0j
    
# S=[]
# for i in range(16):
#     S.append(X[i][0]+X[i][1]j)
    
fig, ax=plt.subplots()
ax.arrow(-3.2,0,6.4,0, head_width=0.2, head_length=0.2)
ax.arrow(0,-4,0,7, head_width=0.2, head_length=0.2)
ax.scatter(np.real(X),np.imag(X), color='r', s = 85)  
# ax.grid(True, which='both')
# ax.axhline(y=0, ls=':')
# ax.axvline(x=0, ls=':')
#   


# x1=np.linspace(-20,20,41)
# x2=np.linspace(-20,20,41)
# x3,x4=np.meshgrid(x1,x2)
G=[[1,0], [1/2, np.sqrt(3)/2]]
# U=[-1,2]
P=[]
n=7
for i in range(-n,n):
    for j in range(-n,n):
        U=[i,j]
        P.append(np.matmul(arr(U),arr(G)))

p=[]
for i in range((2*n)**2):
    p.append(complex(P[i][0],P[i][1]))
    
# p=[]
# for i in range((2*n)**2):
#     if P[i][0]<=3 and P[i][1]<=3 and P[i][0]**2+P[i][1]**2<=9:
#         PP=complex(P[i][0],P[i][1])
#     else:
#         PP=complex(0,0)
#     p.append(PP)    

# plt.figure()
# plt.scatter(np.real(P),np.imag(P), color='b') 

ax.scatter(np.real(p),np.imag(p), facecolors='none', edgecolors='c', s = 110) 
plt.xlabel('Inphase')
plt.ylabel('Quadrature')
plt.xlim(-3.2,3.39)
plt.ylim(-3,3.23)
plt.xticks(visible = False)
plt.yticks(visible = False)
ax.axis("off")
plt.savefig('16A2.eps')


"""ATMA"""
# file=open('16A2_ATMA.txt','w+')
# for A in X:
#     for B in X:
#         file.writelines('{}\t{}\t{}\t{}\n'.format(np.real(A), np.imag(A), np.real(B), np.imag(B)))
# file.close()



# a=2.1
# teta=np.pi/85
# rot_mat=[[np.cos(teta),np.sin(teta)],[-np.sin(teta),np.cos(teta)]]
# X_ATMA=[]
# X_ATMA.append([a,a/2,-a/2,-a,-a/2,a/2,a])
# X_ATMA.append([0,np.sqrt(3)/2*a,np.sqrt(3)/2*a,0,-np.sqrt(3)/2*a,-np.sqrt(3)/2*a,0])
# X_ATMA=arr(rot_mat)@X_ATMA
# X_ATMA=X_ATMA+0.08
# plt.plot(X_ATMA[0],X_ATMA[1])
# plt.axis('equal')
# plt.figure()
circle=plt.Circle((0,0), radius=2,  color='b', fill=False)
ax.add_patch(circle)



"""Regular Hexagon"""
# from matplotlib.patches import RegularPolygon as RP
# add a Polygon
# hex = RP((0,0),numVertices=6, radius=2.5, orientation=0, alpha=0.2, edgecolor='k')
# ax.add_patch(hex)




# """Regular Hexagon with Turtle!"""
# # import the turtle modules
# import turtle

# # Start a work Screen
# ws = turtle.Screen()

# # Define a Turtle Instance
# geekyTurtle = turtle.Turtle()

# # executing loop 6 times for 6 sides
# for i in range(6):

#  	# Move forward by 90 units
#  	geekyTurtle.forward(90)

#  	# Turn left the turtle by 300 degrees
#  	geekyTurtle.left(300)





