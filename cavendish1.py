# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 20:15:01 2021

@author: Petr
"""
import random
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import Model
from min_ctverce import *

def fit_function(t,A,delta,T,phi,S):
    return (A*np.exp(-delta*t)*np.sin(2*np.pi*t/T +phi) + S)


casS1 = []
casS2 = []
nasob = 1
chybat = []
f = open("C:\\Users\\Petr\\Desktop\\Cavend_S1.txt")
dataS1 = []
chybyS1 = []
f1 = f.readlines()
for x in f1:
    chybat.append(0.3)
    a = x.split(";")
    casS1.append(nasob*20)
    nasob += 1 
    chybyS1.append(float(a[1]))
    dataS1.append(float(a[0]))

f= open("C:\\Users\\Petr\\Desktop\\Cavend_S2.txt")
dataS2 = []
chybyS2 = []
nasob = 1
f1 = f.readlines()
for x in f1:
    casS2.append(nasob*20)
    nasob += 1 
    a = x.split(";")
    chybyS2.append(float(a[1]))
    dataS2.append(float(a[0]))

for i in range(len(casS1)):
    c = random.randint(30,50)/100
    rozhoz = random.randint(0,1)
    if(rozhoz):
        casS1[i] += c
    else:
        casS1[i] -= c

chybyS1 = np.array(chybyS1)
casS1 = np.array(casS1)
dataS1 = np.array(dataS1)
p0 = [10,2e-04,200,30,120]
popt,pcov = curve_fit(fit_function,casS1,dataS1,sigma = chybyS1,p0=p0)
sig = np.sqrt(np.diag(pcov))
#plt.scatter(casS1,dataS1,s = 0.4)

plt.figure(figsize = (6.5,4),dpi=150)
plt.errorbar(casS1, dataS1,ecolor='black',color = "red",yerr=chybyS1, fmt = ".k",elinewidth=1,capsize=3,label = "výchylky ")
fit_cas = np.arange(casS1[0],casS1[-1],0.01)
fit_hodnoty = fit_function(fit_cas,*popt)

plt.plot(fit_cas,fit_hodnoty,color = "green",ls=":",label = "$f_{fit} = f(t)$")
pomoc = [139.90272349334325 for i in range(len(fit_cas))]
plt.plot(fit_cas,pomoc,color = "blue",label="$S_1$")
plt.xlabel(r"$t[s]$",size = 14)
plt.ylabel(r"$y[cm]$",size = 14)
plt.title("Závislost polohy světelného bodu na čase \n (rovnovážná poloha $S_1$)")
plt.grid()
plt.legend(fontsize = 12)
plt.ylim(118,168)
plt.savefig("cavendS1.eps")
plt.savefig("cavendS1.pdf")
plt.show()

print("fit1: A = {:5.3f}, delta={:5.3e}, T={:5.3f}, phi = {:5.4f}, S = {:5.3f}".format(*popt))
print("error1: A = {:5.3f}, delta={:5.3e}, T={:5.3f}, phi = {:5.4f}, S = {:5.3f}".format(*sig))
    


    
