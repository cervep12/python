# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 10:57:31 2021

@author: Petr
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:16:43 2021

@author: Petr
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
from lmfit.models import GaussianModel, ExponentialModel
from scipy.optimize import curve_fit
from scipy.special import erf
from lmfit import Model
def asym_peak(x,a0,a1,a2,a3):
    # a0 = pars[0]  # peak area
    # a1 = pars[1]  # elution time
    # a2 = pars[2]  # width of gaussian
    # a3 = pars[3]  # exponential damping term
    f = (a0/2/a3*np.exp(a2**2/2.0/a3**2 + (a1 - x)/a3)*(erf((x-a1)/(np.sqrt(2.0)*a2) - a2/np.sqrt(2.0)/a3) + 1.0))
    return f
def two_peaks(x, a10, a11, a12, a13,a20, a21, a22, a23):
    # a10 = pars[0]  # peak area
    # a11 = pars[1]  # elution time
    # a12 = pars[2]  # width of gaussian
    # a13 = pars[3]  # exponential damping term
    # a20 = pars[4]  # peak area
    # a21 = pars[5]  # elution time
    # a22 = pars[6]  # width of gaussian
    # a23 = pars[7]  # exponential damping term
    p1 = asym_peak(x, a10, a11, a12, a13)
    p2 = asym_peak(x, a20, a21, a22, a23)
    return p1 + p2
def gaussian(x, amp, cen, wid,C):
    return amp * np.exp(-(x-cen)**2 / wid)  + C

w, i = np.loadtxt("C:\\Users\\Petr\\Downloads\\dataGamma3.txt", usecols=(0, 1), unpack=True)
size = 1
gmodel1 = Model(gaussian)
results = gmodel1.fit(i, x= w,amp = 40000, cen =22.9,wid = 120 , C= 100 )
print(results.fit_report())

f, = plt.plot(w, results.best_fit, c="red")
plt.title("Spektrum záření")
plt.xlabel("číslo kanálu")
plt.ylabel('počet událostí')
plt.xlim(0,200)
plt.ylim(0,50000)
ax = plt.gca()
# gmodel2 = Model(two_peaks)
# results = gmodel2.fit(i, x= w,a10 =500000, a11 =3.85,a12 = 0.5, a13 = 0.5,a20 =50000, a21 =27.1,a22 = 5, a23 = 2 )
# print(results.fit_report())
c = plt.scatter(w, i, color="black",zorder = 3,s = size,label = "naměřené hodnoty")
# g, = plt.plot(w, results.best_fit, c="gold",label = "g(x)")
# ind = (w>110) & (w<150)
# #ax.fill_between(w[ind], 0, i[ind], facecolor='gray', alpha=0.5)
# area = np.trapz(i[ind], w[ind])
# x, y = w[ind][np.argmax(i[ind])], i[ind][np.argmax(i[ind])]
# ax.annotate(f'Maximum[{x}, {y}]', xy=(x, y),
#             xycoords='data',
#             xytext=(x + 20, y + 20000),
#             textcoords='data',
#             arrowprops=dict(arrowstyle="->",
#                             connectionstyle="angle,angleA=0,angleB=90,rad=10"))


ind = (w>20) & (w<30)
#ax.fill_between(w[ind], 0, i[ind], facecolor='gray', alpha=0.5)
area = np.trapz(i[ind], w[ind])
x, y = w[ind][np.argmax(i[ind])], i[ind][np.argmax(i[ind])]
ax.annotate(f'Maximum[{x}, {y}]', xy=(x, y),
            xycoords='data',
            xytext=(x + 10, y + 7000),
            textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=10"))
plt.ticklabel_format(axis="y", style="sci", scilimits=(2,3))
plt.legend([c, f],["naměřené hodnoty", r"$y = 220.92 +37990.49 \cdot exp \left(-\frac{(x-21.92)^2}{13.90}\right)$"], loc="right", shadow=True,numpoints=1, labelspacing = 1,bbox_to_anchor=(1,0.5))
plt.savefig("gamma3.eps")
plt.savefig("gamma3.pdf")
plt.show()