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
    return (kvadr/(len(seznam)*((len(seznam)-1))))**0.5

def komb_mereni(chyb_lst, prum_lst):
    citat = 0
    p = 0
    for i in range(len(chyb_lst)):  
        citat += prum_lst[i]*(chyb_lst[i]**(-2))
        p += chyb_lst[i]**(-2)
    vysl = [citat/p, p**(-0.5)]
    return vysl
#def nepr_ch_kyvadlo(l,chl,prumT,prumchybaT):
 #   return ((prumchybaT*8*(math.pi)**2*l/prumT**3)**2+(8*(math.pi)**2 *chl/prumT**2)**2)**0.5
            
#def prum_g_kyv(l,prumT):
 #   return 4*math.pi**2*l/prumT**2 

T = [5,6]
sig = [1,1]

print(komb_mereni(sig,T))





