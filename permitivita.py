# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:15:05 2020

@author: Petr
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import plotly.graph_objects as go
import seaborn as sns
import lmfit
from lmfit import Model

def fit_funkcia(x, A, B):
	return A*x + B
#0.281  0.946  5.764  13.618  16.205  30.140
#C = [0.121*10**(-9),  0.407*10**(-9),  3.073*10**(-9),  4.641*10**(-9),  7.292*10**(-9),  20.979*10**(-9)]
C = [0.281*10**(-9),  0.946*10**(-9),  5.764*10**(-9),  13.618 *10**(-9), 16.205 *10**(-9), 30.140 *10**(-9) ]

a = [0.05,0.10 , 0.20, 0.30, 0.40, 0.50]
S = []
y = []
d = 0.0005

sigm = []
for i in range(len(a)):
    S.append(a[i]**2)
    y.append(C[i]*d)
for i in range(len(y)):
    sigm.append(y[i]*(((0.2)**2 + (0.00001/d)**2)**0.5))
print(y)
print(sigm)
x = np.array(S)
chyba = np.array(sigm)
y = np.array(y)
gmodel = Model(fit_funkcia)
results = gmodel.fit(y, x=x, A=1.8, B=1, weights=1.0/chyba)
print(results.fit_report())
d = plt.scatter(x, y, color="black", zorder=1)
plt.errorbar(x, y, yerr=chyba, fmt=" ", zorder=2, ecolor="black", elinewidth=2.0)
f, = plt.plot(x, results.best_fit, c="red")
plt.legend([d, f],["hodnoty", "y = 5.819$\cdot$10$^{-11}$ $\cdot$ S - 1.184$\cdot$10$^{-14}$ "], loc="upper left", shadow=True)
plt.xlabel("S [m$^{2}$]")
plt.ylabel("y [F$\cdot$m]")
plt.grid()
plt.title("Naměřené hodnoty proložené křivkou \n")
plt.savefig("permitivita_ZFM.eps",format="eps")
plt.savefig("permitivita_ZFM.pdf",format = "pdf")
plt.show()
