# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:51:25 2021

@author: Petr
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
from lmfit import Model
from min_ctverce import *
g = 9.81
R = 1.995/2*10**(-3)
zeta = 3.98*10**(-2)
L = 66.3*10**(-2)
prodl_zatez = [11.5,22,30,35]
prodl_odt = [14,26,31,34,34.5]
zavazi_zat = [0.102,0.203,0.304,0.405]
zavazi_odt = [0.102,0.203,0.304,0.304,0.406]
prodl_zatez = list(map(lambda x: x*math.pi/180, prodl_zatez))
prodl_odt = list(map(lambda x: x*math.pi/180, prodl_odt))
param_odt = min_ctverce( zavazi_odt,prodl_odt)
param_zat =  min_ctverce( zavazi_zat,prodl_zatez)

print(param_zat,param_odt)
x1 = np.linspace(0,0.5,100)
y1 = param_odt[0]*x1+ param_odt[1]
x2 = np.linspace(0,0.5,100)
y2 = param_zat[0]*x2+ param_zat[1]
G_odt = g*L*2*zeta/param_odt[4]/(math.pi*R**4)
G_zat = g*L*2*zeta/param_zat[4]/(math.pi*R**4)
print(G_zat,G_odt)

g1 = plt.scatter(zavazi_odt,prodl_odt,label = 'odtěžování')
g2 = plt.scatter(zavazi_zat,prodl_zatez,label = "zatěžování")
plt.plot(x1,y1, label = "$\Delta \Phi  =1.2\cdot m + 0.2 $")
plt.plot(x2,y2, label = "$\Delta \Phi  =1.36\cdot m + 0.09 $")
plt.legend()
plt.title("Záv. úhlu stočení struny na hmotnosti závaží")
plt.ylabel(r"$\Delta \Phi [rad]$",size = 14)
plt.grid()
plt.xlabel(r"$m [kg]$",size = 14)
plt.ticklabel_format(axis="y", style="sci")
plt.savefig("krutG.eps")
plt.savefig("krutG.pdf")
plt.show()