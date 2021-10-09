# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 13:25:39 2021

@author: Petr
"""

def postup_mer(pul_list,druh_pul_list):
    vysl = []
    soucet = 0
    for i in range(len(pul_list)):
        vysl.append(druh_pul_list[i] - pul_list[i])
        soucet +=druh_pul_list[i] - pul_list[i]
    prumer_vysl = soucet/(len(pul_list))
    soucet = 0
    for i in range(len(pul_list)):
        soucet += (vysl[i] - prumer_vysl)**2
    odchylka = ((soucet/len(pul_list)/(len(pul_list)-1))**0.5)/len(pul_list)
    prumer = prumer_vysl/len(pul_list)
    
    return [prumer,odchylka]
        
    
        