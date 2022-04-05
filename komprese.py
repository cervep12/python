# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 20:48:49 2021

@author: Petr
"""
import math
import numpy as np
from chyba_aritm_prum import *
ref = 192.66
M0 = 96.56
V1 = [191.27,168.70,182.970,170.865,199.635,187.305,184.335,184.275,189.005,186,175.26]
V2 = [186.240,166.8,174.319,161.865,191.817,180.39,178.01,175.01,179.905,176.190,167.045]
TR = [116.120,126.840,116.005,116.920,136.605,136.325,137.607,116.78,120.11,113.15,110.97] 
H = []
M = [210.44,210.24,210.42,210.34,210.48]
T = [21.3,22.0,22.0,22.0,22.2]
for i in range(len(TR)):
    H.append(V2[i] - TR[i]) 
objV1 = list(map(lambda x: round(ref-x,3)/5.215*3.3/5 + 12/5, V1))
objV2 = list(map(lambda x: round(ref-x,3)/5.215*3.3/5 + 12/5, V2))
print("here",objV1[1],objV2[1])
VJ = list(map(lambda t: 0.9998*(1 +0.00018*t),T))
VC = list(map(lambda x,y:(x-M0)*y,M,VJ))
print(np.mean(H)) 
print(np.mean(objV1),np.mean(objV2))
print(np.mean(T))
print(chyba_aritm_prum(T))
V100 = 65.6
p = 101325
g = 9.81
ro = 0.998
V_zas = []
V_nad = []
for i in range(0,2):
    V_zas.append((objV2[i]-objV1[i])*p/ro/H[i]/g + objV2[i] - V100)
for i in range(2,len(V2)):
    V_nad.append((objV2[i]-objV1[i])*p/ro/H[i]/g + objV2[i] - V100)
del V_nad[1]
print("--------------")
print(np.mean(V_zas),np.mean(V_nad),np.mean(VC))
print(chyba_aritm_prum(V_zas), chyba_aritm_prum(V_nad), chyba_aritm_prum(VC))
print(chyba_aritm_prum(M))
for i in range(len(M)):
    M[i] -= 96.56
print("------")
print(np.mean(M),chyba_aritm_prum(M))
print(np.mean(VJ),chyba_aritm_prum(VJ))
print(np.mean(VJ)*np.mean(M))
#a = np.mean(list(map(lambda x:ref-x,V1))[2:len(V1)])
#b = np.mean(list(map(lambda x:ref-x,V2))[2:len(V2)])
#print (a,b)

sigmaV1 = (2*(3.3/5/5.215*10**(-3))**2*(0.000005)**2 + (8.2544*3.3/5*0.000005/0.005215**2)**2)**0.5
print(sigmaV1)
sigmV = 114.2498*((0.0426**2 + 0.52**2)/113.824**2 + 0.1549**2/21.9**2)**0.5
print(sigmV)