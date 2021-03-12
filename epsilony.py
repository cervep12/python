# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:44:05 2020

@author: Petr
"""
import math


x = 0.8
n = math.ceil(2/(1-x))+1
leva = 1-1/n
prava  = x
print("n: "+str(n))
print("prava: "+str(prava))
print("leva: "+str(leva))