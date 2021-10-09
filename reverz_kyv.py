# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:47:56 2021

@author: Petr
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
from lmfit import Model
def fit_funkce(x,A,B,C):
    return A*(x**2) +B*x + C
zavazi = [10.5,12.5,14,17.5,19,21,24,26]
for i in range(len(zavazi)):
    zavazi[i] = zavazi[i]*0.01
cervena =np.array([5.861,5.773,5.709,5.569,5.528,5.535,5.707,5.971])
modra = np.array([5.710,5.668,5.625,5.619,5.580,5.663,5.685,5.718])
gmodel1 = Model(fit_funkce)
gmodel2 = Model(fit_funkce)
results1 = gmodel1.fit(cervena, x=zavazi, A=0.8,C=1,B=1)
print(results1.fit_report())
d1 = plt.scatter(zavazi, cervena, color="black", zorder=2, label = "hodnoty pro osu1")
f1, = plt.plot(zavazi, results1.best_fit, c="black",label = r"$f~({d}_{mag})$")

results2 = gmodel2.fit(modra, x=zavazi, A=0.10,C=1,B=1)
print(results2.fit_report())
d2 = plt.scatter(zavazi, modra, color="red", zorder=2,label="hodnoty pro osu2",marker = "x")
f2, = plt.plot(zavazi, results2.best_fit, c="red",label = r"$g~({d}_{mag})$")
f2.set_linestyle("--")
ax1 = plt.axvline(0.1438852,label='x = 0.1439')
ax2 = plt.axvline(0.22271,label='x = 0.2227')
ax1.set_linestyle("-.")
ax2.set_linestyle("dotted")
plt.legend()
plt.title("Závislost času kmitání rev. kyvadla na poloze magnetu")
plt.ylabel(r"$t[s]$", fontsize=12)
plt.grid()
plt.xlabel(r"${d}_{mag}[m]$",fontsize=12)
plt.savefig("rev_kyv.eps",format="eps")
plt.savefig("rev_kyv.pdf",format="pdf")


# def func(Xe):
#     z = 17.606*Xe**2 - 6.279*Xe + 6.171 - (63.025*Xe**2 - 22.975*Xe + 7.633)
#     return z

# X0 = 0.14
# Xe, = fsolve(func,X0)
# Xf, = fsolve(func,0.22)
# print(f"bbbbbbbbbb{Xf}")
# print(f"aaaaaaaa{Xe}")

# xi = [0.143885,0.2237142]
# yi = interp1d(zavazi ,cervena,"cubic")
# print(yi(xi))
plt.show()