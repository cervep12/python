# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:59:08 2021

@author: Petr
"""
import random
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import Model
from min_ctverce import *
x1 = np.full(50,15)
x2=np.linspace(5,30)
x3=np.linspace(5,30)
print(x2)
y1 = np.linspace(0,0.3)
print(len(y1),len(x1))
y2 = []
y3 = []
for i in range(len(x2)):
    y2.append(3.8/x2[i])
    y3.append(120/(x3[i])**3)
    

a = plt.plot(x1,y1,label = "izochora")
b = plt.plot(x2,y2,label = "izoterma")
c = plt.plot(x3,y3, label = "adiabata")
plt.ylabel("p",size = 14)
plt.xlabel("V",size = 14)
plt.legend(fontsize = 14)
ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])
ax.axes.yaxis.set_ticklabels([])
ax.annotate(r"$stav ~A~(p_{atm} + a,~V_1,~T_1)$",
            xy=(5.65, 0.68), xycoords='data',
            xytext=(0.28, 0.6), textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=1),
            horizontalalignment='left', verticalalignment='top',size = 13)
ax.annotate(r"$stav ~C~(p_{atm}+b,~V_2,~T_1)$",
            xy=(15, 0.25), xycoords='data',
            xytext=(0.48, 0.43), textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=1),
            horizontalalignment='left', verticalalignment='top',size = 13)
ax.annotate(r"$stav ~B~(p_{atm} ,~V_2,~T_2)$",
            xy=(15, 0.04), xycoords='data',
            xytext=(0.485, 0.24), textcoords='figure fraction',
            arrowprops=dict(facecolor='black', shrink=1),
            horizontalalignment='left', verticalalignment='top', size = 13)
plt.savefig("diagr.eps")
plt.savefig("diagr.pdf")
plt.show()