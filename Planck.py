# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:02:17 2022

@author: Petr
"""

import random
import numpy as np
import math
from math import exp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import Model
from min_ctverce import *
from zfmvyp import *
import pandas as pd
from scipy import odr
from scipy.stats import sem
from scipy.integrate import quad
def pol(x,A,B,C,D,E):
    return A*x**4 + B*x**3 +  C*x**2 + D*x + E
def fit_function2(x,A,B):
    return A*x + B
h =6.626070*10**-34
k = 1.38*10**-23
c = 3*10**8

def fit_function(L,T):
    return 2*5.963463e-17/L**5 /(np.exp(0.0144045/L/T)-1)
def fit_functionsp(p,L):
    T = p
    return 2*5.963463e-17/L**5 /(np.exp(0.0144045/L/T)-1)


data = np.loadtxt("C:\\Users\\Petr\\Desktop\\prvni.txt",delimiter = ";", dtype=float)
cejch= np.loadtxt("C:\\Users\\Petr\\Desktop\\cejchovani.txt",delimiter = ";", dtype=float)

U = cejch[:,0]
I = cejch[:,1]
R = U/I
R0 = 0.2
p = np.array([0.2079,-1.8517,7.826,19.274,-0.968])
uit1 = np.array([4.3,4.76,15])
uit2 = np.array([3.92,4.53,8])
uit3 = np.array([5.03,5.21,8])
uit4 = np.array([6.03,5.75,8])
uit5 = np.array([6.86,6.17,25])
uit6 = np.array([7.42,6.44,40])
lS = R0/np.polyval(p,297.25/1000)

rho  = R/lS
root = np.array([])
for i in range(len(rho)):
    p[4] = -0.968-rho[i]
    root = np.append(root,np.roots(p)[2:4])
root = root[1::2]
root = root.real*1000
print(root)
P = U*I
tr = data[:,0]
chytr = data[:,1]

tr1 = tr[0:10]
tr2 = tr[10:20]
tr3 = tr[20:30]
tr4 = tr[30:40]
tr5 = tr[40:50]
tr6 = tr[50:60]

ch1 = chytr[0:10]
ch2 = chytr[10:20]
ch3 = chytr[20:30]
ch4 = chytr[30:40]
ch5 = chytr[40:50]
ch6 = chytr[50:60]

filtry = np.array([420,430,470,500,530,570,610,660,720,750])*10**-9


Iref1 = (tr1/15)*2*h*c**2/filtry**5  /(np.exp(h*c/k/filtry/997.617)-1)
Iref2  = (tr2/8)*2*h*c**2/filtry**5 /(np.exp(h*c/k/filtry/963.437)-1)
Iref3  = (tr3/8)*2*h*c**2/filtry**5 /(np.exp(h*c/k/filtry/1052.86)-1)
Iref4  = (tr4/8)*2*h*c**2/filtry**5 /(np.exp(h*c/k/filtry/1125.9)-1)
Iref5  = (tr5/25)*2*h*c**2/filtry**5 /(np.exp(h*c/k/filtry/1180.57)-1)
Iref6  = (tr6/40)*2*h*c**2/filtry**5 /(np.exp(h*c/k/filtry/1215.21)-1)

sigI1 = Iref1*ch1/tr1
sigI2 = Iref2*ch2/tr2
sigI3 = Iref3*ch3/tr3
sigI4 = Iref4*ch4/tr4
sigI5 = Iref5*ch5/tr5
sigI6 = Iref6*ch6/tr6

sigx = np.array([10,10,10,10,10,10,10,10,10,10])*10**-9*2

plt.figure(figsize = (5.5,3),dpi = 250)

plt.errorbar(filtry, Iref1,fmt = ".k", yerr =sigI1,xerr = sigx,label = "$naměřené~hodnoty$")

lop = odr.RealData(filtry,Iref1,sy = sigI1,sx = sigx)

quad_model = odr.Model(fit_functionsp)
odr1 = odr.ODR(lop, quad_model,beta0 =[1036])
out = odr1.run()

popt = out.beta
perr = out.sd_beta
print("fit parameter 1-sigma error")
print("———————————–")
for i in range(len(popt)):
    print(str(popt[i]) + " +- " + str(perr[i]))


a = np.linspace(40*10**-9,10000*10**-9,1000)
fit = fit_functionsp([popt[0]],a)
plt.plot(a,fit,color = "red",label = "$I = I(\lambda) $")
plt.text(50*10**-7, 4*10**6, '$T = (1040.3 \pm 1.4)~\mathrm{K}$',color = "red", fontsize = 12)

plt.ylabel("$I~\mathrm{[W\cdot m^{-2}]}$",size = 11)
plt.xlabel("$\lambda~\mathrm{[m]}$",size = 11)

plt.legend(fontsize = 11)

plt.savefig("Planck1.eps",bbox_inches='tight')

def g2(x):
    return 2*5.963463e-17/x**5 /(np.exp(0.0144045/x/1115.3)-1)
v = np.linspace(10**-17,90000*10**-7,8000000)
I2 = quad(g2,10**-17,90000*10**-7)
x = g2(v)
I1 = trapz(x,v)
print(I1,I2)
print((I1/5.76*10**8)**0.25,(I2[0]/5.76*10**8)**0.25)

sig = [1.4,1.7,1.4,1.2,2.7,1.7]
# plt.figure(figsize = (6.5,4),dpi = 250)


# plt.scatter(root,U/I ,color = "black",label = r"$R = \left(\frac{U}{I}\right)_{naměř}$")
# k = R0*(1+4.5*10**-3*(root-297.25))
# plt.scatter(root,R0*(1+4.5*10**-3*(root-297.25)),color = "blue",marker = "x",label = r"$R = R_0(1+\alpha \Delta T)$")
# plt.xlabel("$T~\mathrm{[K]}$",size = 11)
# plt.ylabel("$R~\mathrm{[\Omega]}$",size = 11)
# p03 = [100,100,20,20,20]
# popt3,pcov3 = curve_fit(pol,root/1000,U/I,p0=p03)
# sig3 = np.sqrt(np.diag(pcov3))

# a = np.linspace(500,1200,1000)
# fit = pol(a,popt3[0]*10**-12,popt3[1]*10**-9,popt3[2]*10**-6,popt3[3]*0.001,popt3[4])
# plt.plot(a,fit,color = "red",label = r"$R  = P_4(T)$")
# print("chyby:",sig3)
# print("param:",popt3)
# lgd = plt.legend(fontsize = 11)

# plt.savefig("zarov1.eps")


p03 = [100,100]
popt3,pcov3 = curve_fit(fit_function2,root**4,P,p0=p03)
sig3 = np.sqrt(np.diag(pcov3))
plt.figure(figsize = (6.5,4),dpi = 250)

a = np.linspace(0,1.95*10**12,1000)
fit = fit_function2(a,popt3[0],popt3[1])
plt.plot(a,fit,color = "red",label = r"$P = UI = \beta T^4$")
print("chyby:",sig3)
print("param:",popt3)
plt.scatter(root**4, P,color = "blue",label = "$naměřené~hodnoty$")
plt.xlabel("$T^4~\mathrm{[K^4]}$",size = 11)
plt.ylabel("$P~\mathrm{[W]}$",size = 11)

lgd = plt.legend(fontsize = 11)

plt.savefig("Stef_Boltz.eps")

