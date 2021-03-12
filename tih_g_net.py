# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:32:44 2021

@author: Petr
"""

from numpy import *
import pylab

# get data
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
        
    return (kvadr/(len(seznam)*((len(seznam)-1))))**0.5

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
cas1 = [0.544,0.536,0.540,0.544,0.540,0.534,0.548,0.544,0.540,0.544]
cas2= [0.444,0.434,0.452,0.436,0.440,0.452,0.452,0.444,0.432,0.440]
cas3 = [0.316,0.304,0.308,0.300,0.304,0.300,0.308,0.312,0.308,0.316]

g1 = volp(s1,cas1)
g2 = volp(s2,cas2)
g3 = volp(s3,cas3)
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
y = []
y.append(prcas1)
y.append(prcas2)
y.append(prcas3)
print(y)

sigm = []
sigm.append(10*odchylka(cas1,prcas1))
sigm.append(10*odchylka(cas2,prcas2))
sigm.append(10*odchylka(cas3,prcas3))
print(sigm)

x = array([1.505,1.021,0.485])
sigm = array(sigm)
y = array(y)
"""
# create nth degree polynomial fit
n = 1
zn = polyfit(x,y,n) 
pn = poly1d(zn) # construct polynomial 
"""
# create qth degree polynomial fit
q = 2
zq = polyfit(x,y,q) 
pq = poly1d(zq)

# plot data and fit
xx = linspace(0, max(x), 500)
pylab.plot(xx, pq(xx),'-b')
pylab.errorbar(x, y, sigm, fmt='r.')

# customise graph

pylab.xlabel('x label (unit)')
pylab.ylabel('y label (unit)')

pylab.show()