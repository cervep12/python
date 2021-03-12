# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:09:06 2021

@author: Petr
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import plotly.graph_objects as go
import seaborn as sns
import lmfit
from lmfit.models import QuadraticModel
from lmfit import Model
from scipy.optimize import curve_fit

def prumer(seznam):
    soucet = 0
    pocet = len(seznam)
    for i in range(pocet):
        soucet += seznam[i]
    return soucet/pocet  
def odchylka(seznam,prumer):
    kvadr = 0
    for i in range(len(seznam)):
        kvadr += (seznam[i]-prumer)**2
        
    return (kvadr/(len(seznam)*(len(seznam)-1)))**0.5

def volp(draha,casy):
    vysl = []
    for i in range(len(casy)):
        vysl.append(2*draha/(casy[i])**2)
    return vysl


def quadratic(x, A, B,C):
	return (A*x*x + B*x + C)

s1 =1.505
s2=1.021
s3= 0.485
s4 = 0.295
cas1 = [0.544,0.536,0.540,0.544,0.540,0.534,0.548,0.544,0.540,0.544]
cas2= [0.444,0.434,0.452,0.436,0.440,0.452,0.452,0.444,0.432,0.440]
cas3 = [0.316,0.304,0.308,0.300,0.304,0.300,0.308,0.312,0.308,0.316]
cas4 = [0.236,0.240,0.238,0.240,0.236,0.248,0.244,0.240,0.238,0.244]
prcas4 = prumer(cas4)
g1 = volp(s1,cas1)
g2 = volp(s2,cas2)
g3 = volp(s3,cas3)
g4 = volp(s4,cas4)
prumer1 =prumer(g1)
prumer2 =prumer(g2)
prumer3 =prumer(g3)
prcas1 = prumer(cas1)
prcas2 = prumer(cas2)
prcas3 = prumer(cas3)
prumer = []
prumer.append(prumer1)
prumer.append(prumer2)
prumer.append(prumer3)
x = []
x.append(prcas1)
x.append(prcas2)
x.append(prcas3)
x.append(prcas4)
print(x)

sigm = []
sigm.append(10*odchylka(cas1,prcas1))
sigm.append(10*odchylka(cas2,prcas2))
sigm.append(10*odchylka(cas3,prcas3))
sigm.append(10*odchylka(cas4,prcas4))
print(sigm)

y = np.array([1.505,1.021,0.485,0.295])
sigm = np.array(sigm)
x = np.array(x)

gmodel = Model(quadratic)
results = gmodel.fit(y, x= x, A=0, B=0,C=0,weights=1.0/sigm)
print(results.fit_report())
d = plt.scatter(x, y, color="black", zorder=2)
plt.errorbar(x, y, xerr=sigm, fmt=" ", zorder=2, ecolor="black", elinewidth=2.0)
f , = plt.plot(x, results.best_fit, c="red")

plt.legend([d, f],["hodnoty", "s = 4.71 $\cdot t^2$  + 0.34$\cdot t$ - 0.06"], loc="upper left", shadow=True)
plt.xlabel("t [s]")
plt.ylabel("s [m]")
plt.grid(True)
plt.title("Naměřené hodnoty proložené křivkou \n")
plt.savefig("tihg_ZFM.eps",format="eps")
plt.savefig("tihg_ZFM.pdf",format = "pdf")
plt.show