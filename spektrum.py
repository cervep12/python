# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:31:05 2022

@author: Petr
"""
import random
import numpy as np
import math
import scipy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import Model
from min_ctverce import *
from zfmvyp import *
def fit_func(x,A,B,C):
    return A + B/(x - C)
def fit_func2(x,A,B):
    return -1/A/x + 1/B**2

phi = np.array([120.527,120.395,120.404,120.353,120.5])/2*np.pi/180
rtut = np.array([102.864,102.503,100.996,98.852,97.505,96.885,96.196,95.417])/2*np.pi/180
vodik = np.array([100.983,99.009,97.41,95.793])/2*np.pi/180
lambda_rt = np.array([404.7,407.8,435.8,491.6,546.1,578.0,623.4,690.7])
sodik = np.array([96.791,96.734])/2*np.pi/180
prum = np.mean(phi)
# chyb = sem(phi)
# print(prum,chyb)

n = np.sin((rtut + prum)/2)/np.sin(prum/2)

plt.figure(figsize = (6.5,4),dpi = 300)

plt.grid()
plt.ylabel(r"$n^{-2}~\mathrm{[1]}$",size = 13)
plt.xlabel(r"$\lambda~\mathrm{[nm]}$",size = 13)

# plt.scatter(y = 1.63997592,x = 436.15336587,marker = "^",s = 50,color = "green",label = "$vodík$")
# plt.scatter(y = 1.63015423,x=486.597012,marker = "^",s = 50,color = "green")
# plt.scatter(y = 1.613894,x=655.907793,marker = "^",s = 50,color = "green")
# plt.scatter(y=1.622109,x=549.88213,marker = "^",s = 50,color = "green")
# plt.scatter(lambda_rt,n,color ="black",marker = "x",s=80,label = r"$data~rtuť$")
p01 = [10,20,100]
popt1,pcov1 = curve_fit(fit_func,lambda_rt,n,p0=p01)
sig1 = np.sqrt(np.diag(pcov1))
# a = np.linspace(400,720,1000)
# fit = fit_func(a,popt1[0],popt1[1],popt1[2])
# plt.plot(a,fit,color = "red",label = "$n = n(\lambda) $")
print("chyby:",sig1)
print("param:",popt1)
# plt.legend(fontsize = 13)
# plt.savefig("spektrum1.eps")




n_sodik = np.sin((sodik + prum)/2)/np.sin(prum/2)

lambda_sodik = popt1[1]/(n_sodik - popt1[0]) + popt1[2]
dn = abs(n_sodik[0] - n_sodik[1])/abs(lambda_sodik[0]-lambda_sodik[1])
print(lambda_sodik)
n_vodik = np.sin((vodik + prum)/2)/np.sin(prum/2)
print(n_sodik)
lambda_vodik = (popt1[1]/(n_vodik - popt1[0]) + popt1[2])
print(lambda_vodik)
print(dn)


sig = ((11*10**(-12)/(n_vodik - 1.589)**2)**2 + (8*10**-9)**2 + (0.7 * 10**(-9)/(n_vodik - 1.589))**2)**0.5*10**9
sig_s = ((11*10**(-12)/(n_sodik - 1.589)**2)**2 + (8*10**-9)**2 + (0.7 * 10**(-9)/(n_sodik - 1.589))**2)**0.5*10**9
print(sig_s)
# rydb = np.array([0.010977154255088026, 0.009699048820344095,0.009786136704305127,0.010317480333736098])*10**9
# rydb = rydb[::-1]
# print(np.mean(rydb),sem(rydb))
# print(rydb)
# sig_ryd = rydb*sig/lambda_vodik*10**9
# print(komb_mereni(sig_ryd, rydb))

# y = np.array([1/36,1/25,1/16,1/9])
# plt.errorbar(lambda_vodik,y,xerr = sig,fmt = ".k",marker = "x", capsize = 3, capthick = 1,label = r"$data~vodík$")
# p02 = [1/100,2]
# popt2,pcov2 = curve_fit(fit_func2,lambda_vodik,y,sigma = sig,p0=p02)
# sig2 = np.sqrt(np.diag(pcov2))
# a = np.linspace(400,700,1000)
# fit2 = fit_func2(a,popt2[0],popt2[1])
# plt.plot(a,fit2,color = "red",label = "$n^{-2} = f(\lambda)$")
# print("chyby:",sig2)
# print("param:",popt2)
# plt.legend(fontsize = 13)
# plt.savefig("spektrum2.eps")


