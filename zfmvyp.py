# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:37:15 2021

@author: Petr
"""
import numpy as np
import math
from scipy.stats import sem

def prumer(seznam):
    soucet = 0
    pocet = len(seznam)
    for i in range(pocet):
        soucet += seznam[i]
    return soucet/pocet  
def odchylka(seznam,prumer):
    kvadr = 0
    prom = 0
    for i in range(len(seznam)):
        kvadr += (seznam[i]-prumer)*(seznam[i]-prumer)
    vysl = kvadr/(len(seznam)-1)/len(seznam)
    return math.sqrt(vysl)
    #return (kvadr/(len(seznam)*((len(seznam)-1))))**0.5

def volp(draha,casy):
    vysl = []
    for i in range(len(casy)):
        vysl.append(2*draha/(casy[i])**2)
    return vysl

def komb_mereni(chyb_lst, prum_lst):
    citat = 0
    p = 0
    for i in range(len(chyb_lst)):  
        citat += prum_lst[i]*(chyb_lst[i]**(-2))
        p += chyb_lst[i]**(-2)
    vysl = [citat/p, p**(-0.5)]
    return vysl
def neprima_ch(s,prumt,chybat):
    return abs(s/(prumt**3)*4*chybat)


s1 =1.505
s2=1.021
s3= 0.485
s4 = 0.295
cas1 = [0.544,0.536,0.540,0.544,0.540,0.534,0.548,0.544,0.540,0.544]
cas2= [0.444,0.434,0.452,0.436,0.440,0.452,0.452,0.444,0.432,0.440]
cas3 = [0.316,0.304,0.308,0.300,0.304,0.300,0.308,0.312,0.308,0.316]
cas4 = [0.236,0.240,0.238,0.240,0.236,0.248,0.244,0.240,0.238,0.244]

prcas4 = prumer(cas4)
prcas1 = prumer(cas1)
prcas2 = prumer(cas2)
prcas3 = prumer(cas3)
volp1 = volp(s1,cas1)
volp2= volp(s2,cas2)
volp3= volp(s3,cas3)
volp4= volp(s4,cas4)
odchcas1 = odchylka(cas1,prcas1)
odchcas2 = odchylka(cas2,prcas2)
odchcas3 = odchylka(cas3,prcas3)
odchcas4 = odchylka(cas4,prcas4)
g1 = prumer(volp1)
g2= prumer(volp2)
g3= prumer(volp3)
g4= prumer(volp4)
print(g1,g2,g3,g4)
print(neprima_ch(s1,prcas1,odchcas1))
print(neprima_ch(s2,prcas2,odchcas2))
print(neprima_ch(s3,prcas3,odchcas3))
print(neprima_ch(s4,prcas4,odchcas4))

chyby = [0.05,0.11,0.12,0.10]
prum= [10.27,10.43,10.26,10.22]
print(komb_mereni(chyby,prum))








