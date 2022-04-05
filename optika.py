# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:08:47 2022

@author: Petr
"""

import random
import numpy as np
import math
from math import exp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from lmfit import Model
from min_ctverce import *
from zfmvyp import *
import pandas as pd
from scipy import odr
from scipy.stats import sem
def Bessel(e,d):
    return (e**2-d**2)/4/e

y = np.array([ 99.55,99.55,99.55,99.55,98.23])
mat = np.array([20,15,10,5,23.41])
coc1 = np.array([69.88,61.56,72.79,73.68,63.65])
coc2 = np.array([48.78,42.41,35.64,30.35,57.95])
a1_ = coc1 -mat
a2_= coc2 - mat
a1 = y - coc1 
a2 = y - coc2 
d = coc1 - coc2
e = y - mat
sigf = d/2/e*0.3*2**0.5

bessel = Bessel(e,d)
print(komb_mereni(sigf,bessel))


plt.figure(figsize = (6.5,4),dpi = 300)

angle = np.linspace( 0 , 2 * np.pi , 150 )
radius = 1.5
 
x = radius * np.cos( angle ) + 18.4
y = 1.5*radius * np.sin( angle ) +18.4
plt.plot( x, y,label = "$r = 1.5~\mathrm{cm}$" ) 
colors = ["red","blue","black", "green", "brown"]
#plt.scatter( 19.4 , 19.6 , s=8000 ,  facecolors='none', edgecolors='blue' )
for i in range(len(a1)):
    a = np.linspace(3,35,1000)
    func1 = -a1_[i]/a1[i]*a + a1_[i]
    func2 = -a2_[i]/a2[i]*a + a2_[i]
    #plt.plot(a,func1,color = "red",label = "$I = 1.48\\cdot s + 0.002 $")
    plt.plot(a,func2,color = colors[i],label = "$g_{0}$".format(i+1))
plt.xlabel("$x~\mathrm{[cm]}$",size = 11)
plt.ylabel("$y~\mathrm{[cm]}$",size = 11)
plt.axvline(x = 18.4,color = "black",ls = ":",label = "$x = 18.4~\mathrm{cm}$")
plt.axhline(y = 18.4,color = "black",ls = "-.",label = "$y = 18.4~\mathrm{cm}$")
lgd = plt.legend(fontsize = 11)

plt.savefig("cocka.eps")

#rams----------------------------------------------
Rams= 92
Mik = 92.1
okR1 = np.array([83.9,85.21,83.20,79.83,82.64])
okR2 =np.array([36.83,32.48,41.15,47.46,43.32])
okM2 = np.array([30,25.21,35.57,38.24,27.49])
okM1 = np.array([81.76,70.19,80.71,80.62,78.83])
pozorovatkoR = np.array([10,5,15,20,17])
pozorovatkoM = np.array([10,5,15,17,7])
fRams = Bessel(Rams-pozorovatkoR-28.11,okR1-okR2)
fMikr = Bessel(Mik-pozorovatkoM-28.11,okM1-okM2)
print(fMikr)
print("rams: " + str(np.mean(fRams)) + " +- "+ str(sem(fRams)))
print("mik: " + str(np.mean(fMikr)) + " +- "+ str(sem(fMikr)))
#lupa------------------------------------
f_ = (25 + 0.2)
Z = 25/np.mean(fRams)  
print("luopa: ",Z, Z*((sem(fRams)/np.mean(fRams))**2 + (1/25)**2)**0.5)
#tluste cocky [pristoj, predmet]-----------------------------------predmet primi v ohnisku?
mikr = [83.38,88.88]
rams = [85.63,88.63]
oh_rovMikr = 2.8 #mikr[1] - mikr[0]
oh_rovRams = rams[1] - rams[0]
print(oh_rovMikr,oh_rovRams)
#zvetseni mikroskop ------------------------------------------------------
vzd_cocek= 15.9 #vzd rams a  
Delta = vzd_cocek - oh_rovMikr-oh_rovRams
#Z2 = (Delta + oh_rovMikr)/(oh_rovMikr)
Z_mik = 25*((Delta)/ oh_rovMikr/oh_rovRams)
print(Z_mik, ( (25/oh_rovMikr/oh_rovRams*0.2)**2+(25*(oh_rovMikr - 15.9)*0.3/oh_rovRams**2/oh_rovMikr)**2+(25*(oh_rovRams - 15.9)*2**-0.5/oh_rovRams/oh_rovMikr**2)**2)**0.5)
#zvetseni dalekohled--------------------------------------------------------
f1 = 19.2
f2 = 3
Z  = f1/f2
a = 9.449
Z_ = Z*a/(a - 0.192)
print("dalekholed: ",Z,Z_)
print(((1/f2*0.003)**2+(f1/f2**2*2**-0.5)**2)**0.5)
print(((a/(a - 0.192)*1.5)**2+(Z*a/(a-0.192)**2*0.003)**2)**0.5)













