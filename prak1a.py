# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:37:06 2021

@author: Petr
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
from lmfit import Model
from min_ctverce import *
delka = 0.96
m_0 = 0.101
g = 9.81
prum_drat = 0.25*10**(-3)
prodl_zatez = [19.5,29,42,53.5,62.6,71.8,84]
prodl_odt = [25,32.5,44.2,54,65.2,75.5,84.5]
zavazi = [0.102,0.203,0.304,0.406,0.507,0.609,0.710]
zavazi = list(map(lambda x: x+m_0, zavazi))
prodl_zatez = list(map(lambda x: x*10**(-5), prodl_zatez))
prodl_odt = list(map(lambda x: x*10**(-5), prodl_odt))

param_odt = min_ctverce(zavazi,prodl_odt)
param_zat =  min_ctverce(zavazi,prodl_zatez)
print(param_odt,param_zat)
E_odt = 1/param_odt[0]*delka*g/math.pi/(prum_drat/2)**2
E_zat = 1/param_zat[0]*delka*g/math.pi/(prum_drat/2)**2
print(E_zat, E_odt)

x1 = np.linspace(0.15,0.9,100)
y1 = param_odt[0]*x1 + param_odt[1]
f1 = plt.plot(x1, y1,label = "$\Delta L = 0.001\cdot m$")
x2 = np.linspace(0.15,0.9,100)
y2 = param_zat[0]*x2 + param_zat[1]
f2 = plt.plot(x2, y2,label = "$\Delta L = 0.001\cdot m$")
g1 = plt.scatter(zavazi,prodl_odt,label = "odtěžování")
g2 = plt.scatter(zavazi,prodl_zatez,label = "zatěžování")
plt.legend()
plt.title("Záv. prodloužení struny na hmotnosti závaží")
plt.ylabel(r"$\Delta L [m]$",size = 14)
plt.grid()
plt.xlabel(r"$m [kg]$",size = 14)
plt.ticklabel_format(axis="y", style="sci", scilimits=(2,3))
plt.savefig("prodlouzeniE.eps")
plt.savefig("prolouzeniE.pdf")
plt.show()


