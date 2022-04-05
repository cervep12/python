# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 18:16:39 2021

@author: Petr
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 21:49:56 2021

@author: Petr
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:15:02 2021

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

def fit_function(x,A,B):
    return A*np.log(x) + B 
def fit_function2(x,A,B):
    return A*x + B

data = np.loadtxt("C:\\Users\\Petr\\Desktop\\balist_konst.txt",delimiter = ";",skiprows=0, dtype=float)


I = data[:,0]
s1 = data[:,1]
s2 = data[:,2]
s = (s1+s2)/2 * 10**(-2)
p03 = [100,100]
popt3,pcov3 = curve_fit(fit_function2,s,I,p0=p03)
sig3 = np.sqrt(np.diag(pcov3))
plt.figure(figsize = (6.5,4),dpi = 250)

a = np.linspace(0.01,0.15,1000)
fit = fit_function2(a,popt3[0],popt3[1])
plt.plot(a,fit,color = "red",label = "$I = 1.48\\cdot s + 0.002 $")
print("chyby:",sig3)
print("param:",popt3)
plt.scatter(s, I,color = "blue",label = "$naměřené~hodnoty~s$")
plt.xlabel("$s[m]$",size = 11)
plt.ylabel("$I[A]$",size = 11)
plt.grid()
lgd = plt.legend(fontsize = 11)

plt.savefig("balist_konst.eps")
plt.show()


