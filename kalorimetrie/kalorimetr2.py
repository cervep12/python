# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 19:08:40 2021

@author: Petr
"""

# -*- coding: utf-8 -*-


import random
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import Model
from min_ctverce import *
import pandas as pd
def fit_function(x, A, B):
	return A*x + B
data = pd.read_csv("C:\\Users\\Petr\\Desktop\\Praktika\\data\\kalorimetr2",delimiter = "\t",names = ['A','B'])
cas = data["A"].to_numpy()
teplota =  data["B"].to_numpy()
# data1 = pd.read_csv("C:\\Users\\Petr\\Desktop\\Praktika\\data\\merneteplovaru_vinklarek",delimiter = "\t",names = ['A','B'])
# cas1 = data1["A"].to_numpy()
# teplota1 =  data1["B"].to_numpy()
# plt.plot(cas1,teplota1)
popt,pcov = curve_fit(fit_function,cas[0:530],teplota[0:530])
sig = np.sqrt(np.diag(pcov))
popt1,pcov1 = curve_fit(fit_function,cas[560:1812],teplota[560:1812])
sig1 = np.sqrt(np.diag(pcov1))
#plt.scatter(casS1,dataS1,s = 0.4)
plt.figure(figsize = (6.5,4),dpi=150)
#plt.errorbar(casS1, dataS1,ecolor='black',color = "red",yerr=chybyS1, fmt = ".k",elinewidth=1,capsize=3,label = "výchylky ")
#fit_cas = np.arange(cas[0],cas[570],0.01)
fit_hodnoty = fit_function(cas[0:1812],*popt)
fit_hodnoty1 = fit_function(cas[0:1812],*popt1)
a = plt.plot(cas,teplota,color = "black", label = "data")
b = plt.plot(cas[0:1812],fit_hodnoty,color = "red",ls=":",label = "$G_{pomoc}$")
c = plt.plot(cas[0:1812],fit_hodnoty1,color = "green",ls=":",label = "$H_{pomoc}$")
inter = plt.plot([23,32],[31.2,27.3],label = "interpolační křivka")
plt.scatter(27.2,29.36,c='r', label = "$[27.20,~29.36]$")

plt.ylabel(r"$T{[°C]}$",size = 14)
plt.xlabel(r"$t[s]}$",size = 14)
plt.legend(fontsize = 11,loc = "center right")
plt.grid(color = "whitesmoke")
plt.savefig("kalor2.eps")
plt.show()

