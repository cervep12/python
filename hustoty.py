# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:47:55 2020

@author: Petr
"""
import pandas as pd
import numpy as np
import math
data1 = np.array([57.91 , 58.40,  58.98 , 58.91  ,57.76 , 56.60 , 57.55])
data2 = np.array([43.27 , 42.51 , 43.38 , 41.94 , 42.73 , 42.68 , 43.12 ])
data3 = np.array([124.84,  129.81 , 127.91 , 127.22  ,126.13])
V = math.pi * 4.28*4.28 * 5.8 / 3 
om = V * math.sqrt((2*0.05/4.28)**2 + (0.08/5.8)**2)
ro = 127/V
print(sum(data1 /len(data1)),data1.std())
print(sum(data2/len(data2)),data2.std())
print(sum(data3 /len(data3)),data3.std())
print(V , om)
print(ro, ro*math.sqrt((2/127)**2+ (om/V)**2))



    