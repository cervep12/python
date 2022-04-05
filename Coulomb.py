# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:03:59 2021

@author: Petr
"""
import random
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from min_ctverce import *
from scipy.misc import derivative
from zfmvyp import *
from scipy import stats
from chyba_aritm_prum import *
import pandas as pd
from lmfit import Model
import decimal

def fit_func(Qkv, A, B):
    return A*Qkv + B

data = pd.read_csv("C:\\Users\\Petr\\Desktop\\coul.txt",delimiter = "\t",names = ['A','B',"C","D"])
vzd= data["A"].to_numpy()
U= data["B"].to_numpy()
F= data["C"].to_numpy()
sig= data["D"].to_numpy()


p04 = [20,1]
popt4,pcov4 = curve_fit(fit_func,(U[0:5])**2, F[0:5],p0=p04,sigma = sig[0:5],absolute_sigma = True)
sig4 = np.sqrt(np.diag(pcov4))

p05 = [20,1]
popt5,pcov5 = curve_fit(fit_func,(U[5:10])**2, F[5:10],p0=p05,sigma = sig[5:10],absolute_sigma = True)
sig5 = np.sqrt(np.diag(pcov5))

p06 = [20,1]
popt6,pcov6 = curve_fit(fit_func,(U[10:15])**2, F[10:15],p0=p06,sigma = sig[10:15],absolute_sigma = True)
sig6 = np.sqrt(np.diag(pcov6))

p07 = [20,1]
popt7,pcov7 = curve_fit(fit_func,(U[15:20])**2, F[15:20] ,p0=p07,sigma = sig[15:20],absolute_sigma = True)
sig7 = np.sqrt(np.diag(pcov7))

p08 = [0.10,3]
popt8,pcov8 = curve_fit(fit_func,(U[20:25])**2, F[20:25],p0=p08,sigma = sig[20:25],absolute_sigma = True)
sig8 = np.sqrt(np.diag(pcov8))

# plt.figure(figsize = (8,5),dpi = 250)
# a = np.linspace(-0.01, 0.195)

# f4 = fit_func(a,*popt4)
# f5 = fit_func(a,*popt5)
# f6 = fit_func(a,*popt6)
# f7 = fit_func(a,*popt7)
# f8 = fit_func(a,*popt8)
# plt.errorbar(U[0:5]**2, F[0:5],marker = "s" ,ecolor='black',color = "blue",yerr=sig[0:5],fmt = ".k",elinewidth=1,capsize=3,label = "$4~cm$",markeredgewidth=0.7,markeredgecolor= "black",markersize = 7)
# plt.errorbar(U[5:10]**2, F[5:10], ecolor='black',color = "chocolate",yerr=sig[5:10], fmt = ".k",elinewidth=1,capsize=3,label = "$5~cm$",markeredgewidth=0.7,markeredgecolor= "black",markersize = 10)
# plt.errorbar((U[10:15])**2, F[10:15], marker = "P",ecolor='black',color = "indigo",yerr=sig[10:15], fmt = ".k",elinewidth=1,capsize=3,label = "$6~cm$",markeredgewidth=1,markeredgecolor= "black",markersize = 8)
# plt.errorbar((U[15:20])**2, F[15:20], marker = "H",ecolor='black',color = "green",yerr=sig[15:20], fmt = ".k",elinewidth=1,capsize=3,label = "$7~cm$",markeredgewidth=0.7,markeredgecolor= "black",markersize = 8)
# plt.errorbar((U[20:25])**2, F[20:25], marker = "D",ecolor='black',color = "red",yerr=sig[20:25], fmt = ".k",elinewidth=1,capsize=3,label = "$8~cm$",markeredgewidth=0.7,markeredgecolor= "black",markersize = 6)
# plt.plot(a,f4,color = "blue",ls=":",label = "$f_{4} = f_4(U^2)$")
# plt.plot(a,f5,color = "chocolate",ls=":",label = "$f_{5} = f_5(U^2)$")
# plt.plot(a,f6,color = "indigo",ls=":",label = "$f_{6} = f_6(U^2)$")
# plt.plot(a,f7,color = "green",ls=":",label = "$f_{7} = f_7(U^2)$")
# plt.plot(a,f8,color = "red",ls=":",label = "$f_{8} = f_8(U^2)$")
# plt.grid(color = "whitesmoke")
# lgd = plt.legend(bbox_to_anchor= (1.02, 1),fontsize = 13)

# plt.ylabel(r"$F[mN]$",size = 13)
# plt.xlabel(r"$U^2[V^2]$",size = 13)
# plt.savefig("coulomb.eps",bbox_extra_artists=(lgd,), bbox_inches='tight')
# plt.show()

print("4cm: " ,popt4,sig4)
print("5cm: " ,popt5,sig5)
print("6cm: " ,popt6,sig6)
print("7cm: " ,popt7,sig7)
print("8cm: " ,popt8,sig8)