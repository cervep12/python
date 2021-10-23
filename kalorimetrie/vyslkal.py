# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 19:25:50 2021

@author: Petr
"""
import numpy as np
from chyba_aritm_prum import *

def kovy(c1,m1,m,t,t1,kal):
    return(m1*c1 + kal)*(t1-t)/m/(t)
def led(c1,m1,m,t,t1,kal):
    return((m1*c1 + kal)*(t1-t)/m - c1*t )
def para(c1,m1,m,t,t1,tv,kal):
    return((m1*c1 + kal)*(t-t1)-m*c1*(tv-t))/(m)
c2= 4181.8
m0 = 0.14858
m1 = 0.21408-0.14858
m2 = 0.26396-0.21408
t1 = (24-0.9)/0.99443

t2 =( 40.4-0.9)/0.99443
t = (28.55-0.9)/0.99443
kal = (m2*c2)*(t2-t)/(t-t1) - m1*c2
print(kal)

tc = (29.36-0.9)/0.99443
m3 = 0.25168 - 0.14858
m4 = (83.49-54.36)*0.001
t4 = (39.5-0.9)/0.99443
t3 = (27.45-0.9)/0.99443
kal2 = (m4*c2)*(t4-tc)/(tc-t3) - m3*c2
print(kal2)
tv = 100+0.03687*(737.313-760)-0.000022*(737.313-760)**2
kalvysl = np.mean([kal,kal2])
print(chyba_aritm_prum([kal,kal2]),kalvysl)
med = kovy(c2,0.24292-m0,0.36412,(19.14-0.9)/0.99443,(23-0.9)/0.99443,kalvysl)
hlinik = kovy(c2,0.24704-m0,0.11436,(19.5-0.9)/0.99443,22.3/0.99443,kalvysl)
mosaz = kovy(c2,0.24432-m0,0.33472,18.2/0.99443,22.3/0.99443,kalvysl)
led = led(c2,0.28018-m0,0.02562,(11.65-0.9)/0.99443,20.9/0.99443,kalvysl)
para = para(c2,0.25168-m0,0.00778,51.4/0.99443,21.9/0.99443,tv,kalvysl)
print(med,hlinik,mosaz,led,para)