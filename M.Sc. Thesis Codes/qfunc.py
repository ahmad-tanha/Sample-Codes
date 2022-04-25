# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:25:29 2020

@author: Ahmad
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import array as arr
from scipy import special 

def qfunc(x):
    return (1/2)*special.erfc(x/np.sqrt(2))
x=np.linspace(-5,5,50)
plt.plot(x,qfunc(x))
