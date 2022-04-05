# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:55:52 2021

@author: Petr
"""

import random
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import Model
from min_ctverce import *
from zfmvyp import *




c = np.array([15.9921813 , 1.02859763])
p = np.array([8.67613681 ,0.39282307 ])
s = np.array([5.73999724 ,0.35596925])
o = np.array([3.6924 ,0.42363])
d = np.array([ 4.38641707 ,0.46451978 ])
a = np.array([4,5,6,7,8])*0.01 
S = np.array([c[0], p[0], s[0] ,o[0], d[0]])*10**13
sigS = np.array([c[1], p[1], s[1] ,o[1], d[1]])*10**13


def fit_func(Qkv, A, B):
    return A*Qkv + B

p04 = [20000000,100000000000]
popt4,pcov4 = curve_fit(fit_func,1/a**2, S,p0=p04,sigma = sigS,absolute_sigma = True)
sig4 = np.sqrt(np.diag(pcov4))
plt.figure(figsize = (6.5,4),dpi = 250)
pom = np.linspace(0, 700)
f4 = fit_func(pom,*popt4)
plt.errorbar(1/a**2, S, ecolor='black',color = "chocolate",yerr=sigS, fmt = ".k",elinewidth=1,capsize=3,label = "$hodnoty~parametrů~A$",markeredgewidth=0.7,markeredgecolor= "black",markersize = 10)
plt.plot(pom,f4,color = "blue",label = "$g = g(a^{-2})$")
plt.grid(color = "whitesmoke")
plt.ylabel(r"$A[N\cdot V^{-2}]$",size = 13)
plt.xlabel(r"$a^{-2}[m^{-2}]$",size = 13)
plt.legend(fontsize = 13)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

plt.savefig("prum_fit.eps")

plt.show()
print("4cm: " ,popt4,sig4)
print(1/8/np.pi/popt4[0]/2, 1/8/np.pi/popt4[0]**2 * sig4[0]/2 )