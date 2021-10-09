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

def komb_mereni(chyb_lst, prum_lst):
    citat = 0
    p = 0
    for i in range(len(chyb_lst)):  
        citat += prum_lst[i]*(chyb_lst[i]**(-2))
        p += chyb_lst[i]**(-2)
    vysl = [citat/p, p**(-0.5)]
    return vysl
def nepr_ch_kyvadlo(l,chl,prumT,prumchybaT):
    return ((prumchybaT*8*(math.pi)**2*l/prumT**3)**2+(8*(math.pi)**2 *chl/prumT**2)**2)**0.5
            
def prum_g_kyv(l,prumT):
    return 4*math.pi**2*l/prumT**2 

x = komb_mereni([0.203,0.4],[496.849,497.412])
print(x)
"""
lr = 0.3
cervena = [5.552,5.651,5.561,5.628,5.532,5.521,5.560,5.531,5.576,5.609]
modra = [5.534,5.639,5.588,5.635,5.644,5.593,5.576,5.631,5.644,5.577]


cervena = list(map(lambda x: x/5, cervena))
modra = list(map(lambda x: x/5, modra))
cervprum = prumer(cervena)
modprum = prumer(modra)
cervodch = odchylka(cervena, cervprum)
mododch = odchylka(modra, modprum)


komb = komb_mereni([cervodch,mododch], [cervprum,modprum])
b = [nepr_ch_kyvadlo(lr, 0.012,cervprum, cervodch),prum_g_kyv(lr, cervprum)]
c = [nepr_ch_kyvadlo(lr, 0.012,modprum, mododch),prum_g_kyv(lr, modprum)]
vysl = [nepr_ch_kyvadlo(lr,0.012 ,komb[0], komb[1]),prum_g_kyv(lr,komb[0])]
print(f"cervena: {b}")
print(f"modr: {c}")
print(f"vysl: {vysl}")

kyv = [47.835, 47.822, 47.960, 47.943, 47.826, 47.873, 47.909, 47.931, 47.884, 47.872]
kyv = list(map(lambda x: x/25, kyv))
kyvprum = prumer(kyv)
kyvodch = odchylka(kyv,kyvprum)

s = 0.92
x = [nepr_ch_kyvadlo(s, 0.005,kyvprum, kyvodch),prum_g_kyv(s, kyvprum)]
print(f"kyvl: {x}")
print("------------")
print(cervodch, cervprum)
print(mododch, modprum)
print(kyvodch, kyvprum)

a= sem(kyv)

print(a)

"""




