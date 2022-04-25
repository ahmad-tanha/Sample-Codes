# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:40:48 2021

@author: Ahmad
"""

import numpy as np

x=[0.4,0.3,0.2,0.1]
y=np.kron(x,[1/8]*8)
print(y)