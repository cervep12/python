# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:45:44 2021

@author: Petr
"""
import math
import numpy as np

def chyba_aritm_prum(seznam):
    suma = 0
    prumer = np.mean(seznam)
    for i in range(len(seznam)):
        suma += (seznam[i]-prumer)**2
    return (suma/len(seznam)/(len(seznam)-1))**0.5