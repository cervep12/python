# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:47:22 2020

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
C = [0.315*10**(-9),  0.912*10**(-9),  3.290*10**(-9),  11.141 *10**(-9), 17.022 *10**(-9), 25.118 *10**(-9) ]

a = [5,10 , 20, 30, 40, 50]
S = []
y = [0.16*10**(-10),0.46*10**(-10),1.65*10**(-10),5.57*10**(-10),8.5*10**(-10),12.56*10**(-10)]
d = 0.05

sigm = [0.03*10**(-10), 0.09*10**(-10),0.3*10**(-10),1*10**(-10),2*10**(-10),3*10**(-10)]
for i in range(len(a)):
    S.append(a[i]**2)
x = np.array(S)
sigm = np.array(sigm)
y = np.array(y)
gmodel = Model(fit_funkcia)
results = gmodel.fit(y, x=x, A=1, B=1, weights=1.0/sigm)
print(results.fit_report())
d = plt.scatter(x, y, color="black", zorder=2)
plt.errorbar(x, y, yerr=sigm, fmt=" ", zorder=1, ecolor="black", elinewidth=2.0)
f, = plt.plot(x, results.best_fit, c="red")
plt.legend([d, f],["hodnoty", "y = (4.76e-13) $\cdot$ S + 3.45e-12 "], loc="upper left", shadow=True)
plt.xlabel("S [cm$^{2}$]")
plt.ylabel("y [F$\cdot$cm]")
plt.grid()
plt.title("Naměřené hodnoty proložené křivkou \n")
plt.savefig("permitivita2_ZFM.eps",format="eps")
plt.savefig("permitivita2_ZFM.pdf",format = "pdf")
plt.show