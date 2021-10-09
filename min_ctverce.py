# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 22:03:06 2021

@author: Petr
"""

def min_ctverce(x_i,y_i):
    suma1 = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    suma5 = 0
    suma6 = 0
    for i in range(len(x_i)):
        suma1 += x_i[i]*y_i[i]
        suma2 += y_i[i]
        suma3 += x_i[i]
        suma4 += (x_i[i])**2
        suma5 += (y_i[i])**2
    a = (len(x_i)*suma1-suma2*suma3)/(len(x_i)*suma4-suma3**2)
    b = (suma2 -suma3*a)/len(x_i)
    for i in range(len(x_i)):
        suma6 += (y_i[i]-b-a*x_i[i])
    
    s_yx = ((suma6)/(len(x_i)-1))**0.5
    s_b = s_yx*((suma3)/(len(x_i)*suma4-suma3**2))**0.5
    s_a = s_yx*(len(x_i)/(len(x_i)*suma4-suma3**2))**0.5
    return [a,b,s_a,s_b,suma1/suma4]

    