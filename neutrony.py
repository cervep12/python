# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:37:59 2020

@author: Petr
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

soubor = open("C:\\Users\\Petr\\Downloads\\03_Ukol_Fe56_CelkovyUcinnyPrurez.txt")
cteni = soubor.readlines()
data = []
krok = []
for i in range(1,len(cteni)):
    #print(cteni[i].split("\t"))
    krok = cteni[i].split("\t")
    krok[2]= krok[2].replace("\n","")
    for i in range(len(krok)):
        krok[i] = float(krok[i])
    data.append(krok)
soubor.close()
E = []
y1 = []
y2 = []
rozdil = []
pomer=[]
for i in range(len(data)):
    E.append(data[i][0])
    y1.append(data[i][1])
    y2.append(data[i][2])
for i in range(len(y1)):
    rozdil.append(y1[i]-y2[i])
    pomer.append((y2[i]-y1[i])/(y1[i]))
    

size = 0.6    
plt.figure()

#fig, ax = plt.subplots()
#ax.tick_params(axis='y')
plt.scatter(E,y1,color = "blue",s=size,label="JEFF 3.3")
#plt.legend(loc = "lower left",scatterpoints = 300, labelspacing = 1, title="Legenda")
plt.xlabel("Energie neutronů [eV]")
plt.ylabel('Účinný průřez [barn]')
#ax.set_xlim([0.01,300000000])
plt.yscale("log")
plt.xscale("log")
plt.grid()

plt.scatter(E,y2,color = "red",s=size,label="ENDF/B-VIII")
plt.legend(loc = "lower left",scatterpoints = 300, labelspacing = 1, title="Legenda")
plt.xlabel("Energie neutronů [eV]")
plt.ylabel('Účinný průřez [barn]')
#ax.set_xlim([0.01,300000000])
plt.yscale("log")
plt.xscale("log")
plt.grid()
plt.title("Srovnání dat knihoven")
plt.grid()
plt.savefig("neutrony3.eps",format="eps")
plt.savefig("Neutrony3.pdf",format = "pdf")

#--------------------------------------------------------------------------

fig, ax1 = plt.subplots()
color = 'lightgreen'
ax1.set_xlabel("Energie neutronů [eV]")
ax1.set_ylabel('Účinný průřez [barn]', color=color)
leg1 = ax1.scatter(E,y1,color = color,s=size,label="JEFF 3.3")
ax1.tick_params(axis='y', labelcolor=color)
plt.yscale("log")
plt.xscale("log")
ax1.set_xlim([0.0001,300000000])
#plt.legend(loc = "center left",scatterpoints = 300, labelspacing = 3.5, title="Legenda")
plt.grid()
ax1.legend(title = "Legenda",loc = "lower center",scatterpoints = 300, labelspacing = 1,bbox_to_anchor=(0.5, -0.4))
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'orange'
ax2.set_ylabel('Relativní odchylka', color=color)  # we already handled the x-label with ax1
leg2 = ax2.scatter(E,pomer,s=size,color = color,label = "rel. odchylka ENDF/B-VIII od JEFF 3.3 ")
ax2.tick_params(axis='y', labelcolor=color)
plt.xscale("log")
plt.grid(color = "orange")
ax2.set_ylim([-1.5,6.5])


ax2.legend(loc = "lower left",scatterpoints = 300, labelspacing = 1,bbox_to_anchor=(0.37,-0.5))
#plt.legend(loc = "center left",scatterpoints = 300, labelspacing = 1)
plt.title("Rel. odchylka dat ENDF/B-VIII od JEFF 3.3 ")
plt.savefig("neutrony2.eps",format="eps",bbox_inches='tight')
plt.savefig("Neutrony2.pdf",format = "pdf",bbox_inches='tight')

#-----------------------------------------------------------------------

fig, ax1 = plt.subplots()
color = 'lightgreen'
ax1.set_xlabel("Energie neutronů [eV]")
ax1.set_ylabel('Účinný průřez [barn]', color=color)
ax1.scatter(E,y1,color = color,s=size,label="JEFF 3.3")
ax1.tick_params(axis='y', labelcolor=color)
plt.yscale("log")
plt.xscale("log")
ax1.set_xlim([0.0001,300000000])
plt.grid()
ax1.legend(title = "Legenda",loc = "lower center",scatterpoints = 300, labelspacing = 1,bbox_to_anchor=(0.5, -0.4))

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'purple'
ax2.set_ylabel('Rozdíl [barn]', color=color)  # we already handled the x-label with ax1
ax2.scatter(E,rozdil,s=size,color = color,label = "rozdíl ENDF/B-VIII a JEFF 3.3")
ax2.tick_params(axis='y', labelcolor=color)
plt.xscale("log")
ax2.set_ylim([-12,8])
plt.grid(color = "pink")

ax2.legend(loc = "lower left",scatterpoints = 300, labelspacing = 1,bbox_to_anchor=(0.37,-0.5))
plt.title("Rozdíl dat ENDF/B-VIII od JEFF 3.3")
plt.savefig("neutrony1.eps",format="eps", bbox_inches='tight')
plt.savefig("Neutrony1.pdf",format = "pdf",bbox_inches='tight')

 # otherwise the right y-label is slightly clipped
plt.show()





    

