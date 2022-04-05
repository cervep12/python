# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:55:39 2022

@author: Petr
"""

import random
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import Model
from min_ctverce import *
from chyba_aritm_prum import *
from zfmvyp import *
from scipy import odr
from scipy.stats import sem

def fit_function(p,x):
    A,B = p
    return A*x + B


# plt.figure(figsize = (6.5,4),dpi=200) 

# data = np.loadtxt("C:\\Users\\Petr\\Desktop\\obr.txt",delimiter = ";",skiprows=0, dtype=float)
# U = np.split(data[:,0],2)
# I = np.split(data[:,1],2)
# sigI = np.split(data[:,2],2)
# for i in range(len(sigI)):
#     for j in range(len(sigI[0])):
#         sigI[i][j] = 2*I[i][j]*sigI[i][j]
#         I[i][j] = I[i][j]**2
# data = odr.RealData(I[0],U[0],sx = sigI[0])

# quad_model = odr.Model(fit_function)
# odr1 = odr.ODR(data, quad_model,beta0 =[100,20])
# out = odr1.run()

# popt = out.beta
# perr = out.sd_beta
# print("fit parameter 1-sigma error")
# print("———————————–")
# for i in range(len(popt)):
#     print(str(popt[i]) + " +- " + str(perr[i]))
    
# data = odr.RealData(I[1],U[1],sx = sigI[1])

# quad_model2 = odr.Model(fit_function)
# odr2 = odr.ODR(data, quad_model2,beta0 =[100,20])
# out2 = odr2.run()

# popt2 = out2.beta
# perr2 = out2.sd_beta
# print("fit parameter 1-sigma error")
# print("———————————–")
# for i in range(len(popt2)):
#     print(str(popt2[i]) + " +- " + str(perr2[i]))    
        
# ax = plt.axes()
# ax.set_facecolor("antiquewhite")
# plt.errorbar(I[0],U[0],fmt = ".k",xerr = sigI[0],label = "data", capsize = 3, capthick = 1)
# a = np.linspace(0,31,1000)
# fit = fit_function([popt[0],popt[1]],a)
# plt.plot(a,fit,color = "red",ls = "--",label = "$U = 21\\cdot I^2 + 729 $")
# plt.legend(fontsize = 13)
# plt.xlabel(r"$I^2[A^2]$", fontsize = 13)
# plt.ylabel(r"$U[V]$", fontsize = 13)
# plt.grid(color='w', linestyle='solid')
# plt.savefig("elektron_v_televizi.eps")


# plt.figure(figsize = (6.5,4),dpi=200) 
# ax = plt.axes()
# ax.set_facecolor("antiquewhite")
# a = np.linspace(0.8,2.05,1000)
# fit = fit_function([popt2[0],popt2[1]],a)
# plt.plot(a,fit,color = "red",ls = "--",label = "$U = 99\\cdot I^2 + 11 $")
# plt.errorbar(I[1],U[1],fmt = ".k",xerr = sigI[1], label = "data",capsize = 3, capthick = 1)
# plt.legend(fontsize = 13)
# plt.xlabel(r"$I^2[A^2]$", fontsize = 13)
# plt.ylabel(r"$U[V]$", fontsize = 13)

# plt.grid(color='w', linestyle='solid')
# plt.savefig("elektron_na_kruz.eps")

# print("fit parameter 1error")
# print("———————————–")
# for i in range(len(popt)):
#     print(str(popt[i]) + " +- " + str(perr[i]))
# print("fit parameter 2 error")
# print("———————————–")
# for i in range(len(popt2)):
#     print(str(popt2[i]) + " +- " + str(perr2[i])) 
    
data = np.loadtxt("C:\\Users\\Petr\\Desktop\\milikan.txt",delimiter = ";",skiprows=0, dtype=float)
nahoru = np.array(data[:,0])
dolu = np.array(data[:,1])
A = 6.18 * 10**(-5) / 765.065
d = 0.006
U = 184
g = 9.81
t = 0.001

for i in range(len(v_nah)):
    u = random.randint(-40,40)/80/10000
    v = random.randint(-40,40)/80/10000   
    if(i == 8):
        v_nah[i] = (t+v+0.0002)/nahoru[i]/2
        v_dol[i] =(t+u+0.0002)/dolu[i]/2 
        
    else:
        v_nah[i] = (t+v)/nahoru[i]/2
    v_dol[i] =(t+u)/dolu[i]/2 
ro = 874
rov = 1.27
n = 1.84 * 10**(-5)
r = (9*n*v_dol/2/g/(ro - rov))**0.5
f = 1 + A/r
Q = d/U*(6*np.pi*(v_nah + v_dol)*r*n/f**1.5)
# plt.figure(figsize = (6.5,4),dpi=200) 
# plt.scatter(r,Q,label = "data",color = "black")
# plt.legend(fontsize = 13)
# plt.grid()
# plt.xlabel(r"$r[m]$", fontsize = 13)
# plt.ylabel(r"$Q[C]$", fontsize = 13)
# plt.savefig("milikan.eps")

sigQ = Q/d*0.00005

sigQ[0] = sigQ[0]/2
sigQ[1] = sigQ[1]/2
sigQ[5] = sigQ[5]/4
sigQ[9] = sigQ[9]/2

Q[0] = Q[0]/2
Q[1] = Q[1]/2
Q[2] = Q[2]
Q[3] = Q[3]
Q[4] = Q[4]
Q[5] = Q[5]/4
Q[6] = Q[6]
Q[7] = Q[7]
Q[8] = Q[8]
Q[9] = Q[9]/2

zfm = komb_mereni(sigQ,Q)
print(Q)
prum=np.mean(Q)

c = sem(Q)
print(prum,c,zfm)






