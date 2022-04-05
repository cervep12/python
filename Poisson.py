# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 19:00:31 2021

@author: Petr
"""

import random
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import Model
from min_ctverce import *

def fit_funkcia(x, A,B):
	return A*x +B

H = [15.4,16.4,16.9,14.3,16.0,15.1,16.4,17.3,16.7,16.9,17.2,16.8]
H_a = [1.9,1.7,3.8,3.4,3.4,3.8,3.9,4.1,3.9,4.3,3.9,3.7]
t = [0.333,0.351,0.265,0.284,0.503,0.244,0.323,0.284,0.343,0.429,0.381,0.481]
kappa = []
kappa2 = []
H2 = [16.9,14.3,16.0,15.1,16.4,17.3,16.7,16.9,17.2,16.8]
H_a2 = [3.8,3.4,3.4,3.8,3.9,4.1,3.9,4.3,3.9,3.7]
t2 = [0.265,0.284,0.503,0.244,0.323,0.284,0.343,0.429,0.381,0.481]
for i in range(len(H)):
    kappa.append((H[i])/(H[i]-H_a[i]))
for i in range(len(H2)):
    kappa2.append((H2[i])/(H2[i]-H_a2[i]))
# t = np.array(t)
# kappa = np.array(kappa)
# t2 = np.array(t2)
# kappa2 = np.array(kappa2)
y1 = []
y2 = []
v = np.linspace(0.22,0.50)

for i in range(len(v)):
    y1.append( -0.07472720*v[i] + 1.30201)
for i in range(len(v)):
    y2.append( -0.117799*v[i] + 1.3469)
gmodel1 = Model(fit_funkcia)
results1 = gmodel1.fit(kappa, x=t, A=0.1,B = 1.5)
print(results1.fit_report())
c = plt.scatter(t, kappa, color="black",label = "naměřené hodnoty")
a = plt.plot(v, y1, color="red",label = "$f_{fit} = f(t)$")

gmodel2 = Model(fit_funkcia)
results2 = gmodel2.fit(kappa2, x=t2, A=0.1,B = 1.5)
print(results2.fit_report())
b = plt.plot(v, y2, color="blue",label = "$g_{fit} = g(t)$")
plt.xlabel("$t~[s]$", size = 14)
plt.ylabel("$\kappa~[1]$", size = 14)
plt.legend(fontsize = 12,facecolor="khaki")
plt.grid()
plt.savefig("kappa.eps",format="eps")
plt.savefig("kappa.pdf",format ="pdf")
plt.show()