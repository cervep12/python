# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 13:10:27 2021

@author: Petr
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
from lmfit import Model
from min_ctverce import *
from postup_mer import *
from chyba_aritm_prum import *
g = 9.81

M = 0.128
Ri = 0.36*10**(-2)
Ro = 2.49*10**(-2)
L = 22.9*10**(-2)
R_dr = 0.49/2*10**(-3)
v1 = 8.44*10**(-3)
v2 = 8.45*10**(-3)
xA1 = 9.59*10**(-2) - v1
xA2 = 9.67*10**(-2) - v2
xB1 = 6.51*10**(-2) - v1
xB2 = 6.53*10**(-2) - v2
IA1 = M/4*(Ri**2 +Ro**2 + 1/3*v1**2 )+ M*(xA1)**2
IA2 = M/4*(Ri**2 +Ro**2 + 1/3*v2**2 )+ M*(xA2)**2
IB1 =M/4*(Ri**2 +Ro**2 + 1/3*v1**2 )+ M*(xB1)**2
IB2 = M/4*(Ri**2 +Ro**2 + 1/3*v2**2 )+ M*(xB2)**2
print(IA1)
print(IB1)
TA = [3.52*2,3.67*2,3.55*2,3.56*2,3.605*2]
TB = [2.64*2,2.64*2,2.62*2,2.62*2,2.63*2]
postup1 = [12.95,26.14,39.4,52.53,65.7]
postup2 = [78.96,92.21,105.34,118.65,131.55]
prTA = float(np.mean(TA))
prTB = float(np.mean(TB))

T = postup_mer(postup1,postup2)
print(T[0],T[1])
print(T[0]*0.4,T[1]*0.4)
I_tyc = (prTA*prTA*(IB1 + IB2)-prTB*prTB*(IA1+IA2))/(prTB**2 - prTA**2)
I_zk = 2*(prTA**2 * IB1 - prTB**2 * IA1)/(prTB**2-prTA**2)
I_c = I_tyc + IB2 + IB1
print(I_tyc)
print(I_c)
G = 8*math.pi * L * I_c/(T[0]*0.4)**2/R_dr**4
print(G)
print(xA1,xA2,xB1,xB2)


