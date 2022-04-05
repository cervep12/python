# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:56:01 2022

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
from scipy import integrate
from scipy.integrate import simps
from scipy.integrate import trapz
from scipy.integrate import quad



data = np.loadtxt("C:\\Users\\Petr\\Desktop\\hyst_krivka_data.txt",delimiter = ";",skiprows=0, dtype=float)



y = np.split(data[:,1],4)
x = np.split(data[:,0],4)

Bm = y[0][0]/2*2.16/4/2.43*0.1
y[0] = Bm - 2.16/4/2.43*y[0]*0.1
y[1] = Bm - 2.16/4/2.43*y[1]*0.1
y[2] = -Bm + 2.16/4/2.43*y[2]*0.1
y[3] = -Bm + 2.16/4/2.43*y[3]*0.1
y = np.concatenate(y)
y[0] = 10.9*2.16/4/2.43*0.1
y[1] = 10.85*2.16/4/2.43*0.1
x = np.concatenate(x)
x = x*62/2/np.pi/17.1*1000

      
    
plt.figure(figsize = (6.5,4),dpi=200)

def fit_func1(x,A,B,C,D):
    return A*np.arctan(B*x + C) + D

#usek 1 zap exp
p01 = [0.1,0.03,0.1,0.001]
popt1,pcov1 = curve_fit(fit_func1,x[0:19],y[0:19],p0=p01)
sig1 = np.sqrt(np.diag(pcov1))

pom1 = np.linspace(-120, 120)
f1 = fit_func1(pom1,*popt1)
plt.plot(pom1,f1,ls = "--",color = "red",label = "$g = g(H)$")

#-------------------------------
#4 usek klad exp
p04 = [0.1,0.03,-0.22,0.001]
popt4,pcov4 = curve_fit(fit_func1,x[20:40],y[20:40],p0=p04)
sig4 = np.sqrt(np.diag(pcov4))


pom4 = np.linspace(-120, 120)
f4 = fit_func1(pom4,*popt4)


plt.plot(pom4,f4,color = "green",ls = "--",label = "$f = f(H)$")


plt.scatter(0,0.1156,marker = "x",s = 80,color = "purple",label = "$B_{r\pm}$")
plt.scatter(0,-0.1104,marker = "x",s = 80,color = "purple")
plt.scatter(-17.6128,0,marker = "^",s = 60,color = "purple")
plt.scatter(17.1521,0,marker = "^",s = 60,color = "purple", label = "$H_{k\pm}$")

plt.grid()
plt.ylabel(r"$B[T]$",size = 13)
plt.xlabel(r"$H[A\cdot m^{-1}]$",size = 13)
plt.legend(fontsize = 13)
#plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
#plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.axvline(x = 0,ymin = -10.1)
plt.axhline(y = 0, xmin = -0.205)
plt.scatter(x[0:19],y[0:19],color ="black",marker = "x",label = "data \"tam\" ")
plt.scatter(x[20:40],y[20:40],color ="black",label = "data \"zpět\" ")



plt.legend(fontsize = 13)
plt.savefig("hystereze.eps")
print("sig1: " , sig1, popt1)
print("sig4: " , sig4, popt4)


#-------------------------
#integrace

#area = trapz(y[0:10],x[0:10])
#area1 = simps(y[0:10],x[0:10])
# print(x,y)
body = np.array([120,-18.4,-120,16.3])
n = 1000

def g1(x):
    return (popt1[0] + 0.003)*np.arctan((popt1[1]-0.003)*x + 0.05 + popt1[2]) + popt1[3]

def g4(x):
    return (popt4[0]+0.003)*np.arctan((popt4[1]-0.003)*x - 0.05 + popt4[2]) + popt4[3]

I1 = quad(g1,body[1],body[0])[0]
I2 = quad(g1,body[2],body[1])[0]
I3 = quad(g4,body[2],body[3])[0]
I4 = quad(g4,body[3],body[0])[0]

print(I1,I2,I3,I4)
usek_nad =  I1 - I4 
usek_pod = I3 - I2
print("nad :" , usek_nad)
print("pod :" , usek_pod)
print("plocha :",usek_nad - usek_pod)
H_m = (np.tan(-popt1[3] /popt1[0]) - popt1[2])/popt1[1]
H_p = (np.tan(-popt4[3]/popt4[0]) - popt4[2])/popt4[1]
B_p = popt1[0]*np.arctan(popt1[2]) + popt1[3]
B_m = popt4[0]*np.arctan(popt4[2]) + popt4[3]
print("B:",(B_p - B_m)/2)
print("H:",(H_p - H_m)/2)

