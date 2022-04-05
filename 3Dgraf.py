# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:48:30 2021

@author: Petr
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import plotly.graph_objects as go
from IPython.display import display, Latex


potenc = np.loadtxt("C:\\Users\\Petr\\Desktop\\potenc_prak.txt",delimiter = "\t",skiprows=1, dtype=float)
potenc1 = potenc[:,0]
potenc2 = potenc[:,1]
for i in range(len(potenc1)):
    potenc1[i] = -potenc1[i]
    potenc2[i] = -potenc2[i]
x = []
y = []
for i in range(1,13):
    for j in range(1,13):
        x.append(i)
        y.append(j)
x = np.array(x)
y = np.array(y)

x = np.reshape(x,(12,12))
y = np.reshape(y,(12,12))
potenc1 = np.reshape(potenc1,(12,12))
potenc2 = np.reshape(potenc2,(12,12))






fig = go.Figure(data=[go.Surface(z=potenc1, x=x, y=y)])
fig.update_layout(title = "Potenciál první konfigurace",scene = dict(
                    
                    xaxis_title="x",
                    yaxis_title="y",
                    zaxis_title= "φ"))
                   
fig.write_html("potenc1.html")
fig = plt.figure(figsize =(15, 11))
ax = plt.axes(projection='3d')
ax.set_xlabel('x',size = 20,labelpad=20)
ax.set_ylabel('y',size = 20,labelpad=20)
ax.set_zlabel("$\\phi$",size = 20,labelpad=10)
ax.zaxis.set_tick_params(labelsize=18)
ax.yaxis.set_tick_params(labelsize=18)
ax.xaxis.set_tick_params(labelsize=18)
ax.zaxis.set_rotate_label(False) 
surf = ax.plot_surface(x, y, potenc1,edgecolor ='none', cmap='plasma', linewidth=1)
cbar = fig.colorbar(surf,ax=ax, shrink=0.5, aspect=5)
cbar.ax.tick_params(labelsize=18)
plt.savefig("potenc1.eps")
fig2 = go.Figure(data=[go.Surface(z=potenc2, x=x, y=y)])
fig2.update_layout(title = "Potenciál druhé konfigurace",scene = dict(
                    
                    xaxis_title="x",
                    yaxis_title="y",
                    zaxis_title= "φ"))
                   
fig2.write_html("potenc2.html")
fig2 = plt.figure(figsize =(15, 11))
ax2 = plt.axes(projection='3d')
ax2.set_xlabel('x',size = 20,labelpad=20)
ax2.set_ylabel('y',size = 20,labelpad=20)
ax2.set_zlabel("$\\phi$",size = 20,labelpad=10)
ax2.zaxis.set_tick_params(labelsize=18)
ax2.yaxis.set_tick_params(labelsize=18)
ax2.xaxis.set_tick_params(labelsize=18)
ax2.zaxis.set_rotate_label(False) 
surf2 = ax2.plot_surface(x, y, potenc2,edgecolor ='none', cmap='plasma', linewidth=1)
cbar2 = fig2.colorbar(surf2,ax=ax2, shrink=0.5, aspect=5)
cbar2.ax.tick_params(labelsize=18)
plt.savefig("potenc2.eps")