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
def asym_peak(x,pars):
    a0 = pars[0]  # peak area
    a1 = pars[1]  # elution time
    a2 = pars[2]  # width of gaussian
    a3 = pars[3]  # exponential damping term
    f = (a0/2/a3*np.exp(a2**2/2.0/a3**2 + (a1 - x)/a3)*(erf((x-a1)/(np.sqrt(2.0)*a2) - a2/np.sqrt(2.0)/a3) + 1.0))
    return f
def gaussian(x, amp, cen, wid):
    return amp * np.exp(-(x-cen)**2 / wid)
w, i = np.loadtxt("C:\\Users\\Petr\\Downloads\\dataGamma1.txt", usecols=(0, 1), unpack=True)
#plt.plot(w, i)
plt.title("Spektrum záření")
plt.xlabel("číslo kanálu")
plt.ylabel('počet událostí')
plt.xlim(0,1000)
plt.ylim(0,14000)
ax = plt.gca()
#ax.annotate('Some typical region', xy=(0, 13000), xycoords='data')
#ax.fill_between([0, 25], 0, [14000, 14000], facecolor='red', alpha=0.25)
gmodel1 = Model(gaussian)
results = gmodel1.fit(i, x= w,amp = 4000,cen = 206,wid = 0.1)
print(results.fit_report())
d = plt.scatter(w, i, color="black",zorder =0.5,s = 2)
f, = plt.plot(w, results.best_fit, c="red")
plt.legend([d, f],["naměřené hodnoty", r"$y = 4777.12 \cdot exp \left(-\frac{(x-207.40)^2}{196.70}\right)$"], loc="upper right", shadow=True,numpoints=1)

# gmodel2 = Model(gaussian)
# results = gmodel2.fit(i, x= w,amp = 10000,cen = 12,wid = 0.1)
# print(results.fit_report())
# c, = plt.plot(w, i, color="black",zorder = 0.5)
# g, = plt.plot(w, results.best_fit, c="green")


# shade the region in the spectrum
ind = (w>190) & (w<210)
#ax.fill_between(w[ind], 0, i[ind], facecolor='gray', alpha=0.5)
area = np.trapz(i[ind], w[ind])
x, y = w[ind][np.argmax(i[ind])], i[ind][np.argmax(i[ind])]
ax.annotate(f'Maximum[{x}, {y}]', xy=(x, y),
            xycoords='data',
            xytext=(x + 50, y + 2000),
            textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=10"))


# # find a max in this region, and annotate it
# ind = (w>120) & (w<180)
# x,y = w[ind][np.argmax(i[ind])], i[ind][np.argmax(i[ind])]
# ax.annotate(f'Area[{x}, {y}]', xy=(x, y),
#             xycoords='data',
#             xytext=(x + 350, y + 4500),
#             textcoords='data',
#             arrowprops=dict(arrowstyle="->",
#                             connectionstyle="angle,angleA=0,angleB=90,rad=10"))

# # find max in this region, and annotate it
# ind = (w>30) & (w<40)
# x,y = w[ind][np.argmax(i[ind])], i[ind][np.argmax(i[ind])]
# ax.annotate(f'Area[{x}, {y}]', xy=(x, y),
#             xycoords='data',
#             xytext=(x + 400, y + 4000),
#             textcoords='data',
#             arrowprops=dict(arrowstyle="->",
#                             connectionstyle="angle,angleA=0,angleB=90,rad=10",color="blue"))
# ind = (w>0) & (w<150)
# x,y = w[ind][np.argmax(i[ind])], i[ind][np.argmax(i[ind])]
# ax.annotate(f'Area[{x}, {y}]', xy=(x, y),
#             xycoords='data',
#             xytext=(x + 100, y + 800),
#             textcoords='data',
#             arrowprops=dict(arrowstyle="->",
#                             connectionstyle="angle,angleA=0,angleB=90,rad=10"))
# ind = (w>50) & (w<80)
# x,y = w[ind][np.argmax(i[ind])], i[ind][np.argmax(i[ind])]
# ax.annotate(f'Area[{x}, {y}]', xy=(x, y),
#             xycoords='data',
#             xytext=(x + 200, y + 2000),
#             textcoords='data',
#             arrowprops=dict(arrowstyle="->",
#                             connectionstyle="angle,angleA=0,angleB=90,rad=10"))

# indicate a region with connected arrows
# ax.annotate('CH bonds', xy=(2780, 6000), xycoords='data')
# ax.annotate('', xy=(2800., 5000.),  xycoords='data',
#             xytext=(3050, 5000), textcoords='data',
#             # the arrows connect the xy to xytext coondinates
#             arrowprops=dict(arrowstyle="<->",
#                             connectionstyle="bar",
#                             ec="k",  # edge color
#                             shrinkA=0.1, shrinkB=0.1))
plt.savefig("gamma1.eps")
plt.savefig('gamma1.pdf')
plt.show()