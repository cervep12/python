# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:27:53 2021

@author: Petr
"""
import random
import math
import copy


jeregular = True

def vytvor_matici(radek,sloupec):
    pomoc_radek = []
    matice = []
    for i in range(sloupec):
        for j in range(radek):
            pomoc_radek.append(random.randint(-5,5))
        matice.append(pomoc_radek)
        pomoc_radek = []
    return matice

#sestav jednotkouvou matici s rozmerem
def jednotkova(rozmer):
    jed = []
    seznam = []
    for i in range(rozmer):
        for j in range(rozmer):
            seznam.append(0)
        seznam[i] = 1
        jed.append(seznam)
        seznam = []
    return jed
        
        

def vypis(matice):
    for i in range(len(matice)):
        print(matice[i])
         
# pocinaje zadanym radkem, najdi ve sloupci s porad cislem index, nenul cislo

def najdi_nenul_cis(matice,radek,index):
    navrat = [-1,-1] # hodnota, index nenul prvku
    for i in range(radek,len(matice)):
        if(matice[i][index] != 0):
            navrat[0] = matice[i][index]
            navrat[1] = i
            break
    return navrat

#prohod radek1 s radekem 2  v matici
def prohod(matice,radek1,radek2):
    menic = matice[radek2]
    matice[radek2]=matice[radek1]
    matice[radek1] = menic

#vydel radek cislem
def vydel(matice,radek,delic):
    if(delic != 0 ):
        for i in range(len(matice[radek])):
            matice[radek][i] = round(matice[radek][i]/delic,4)
            
            
# vezmi 2 radky a pricti nasobek 1 radku k druhemu, tak aby se v radku 2 vynuloval 
# 1. nenulovy clen

def nuluj(matice,radek1,radek2,pozice,matice2 = []):#radek2 + nasobek radek1
    nas = matice[radek2][pozice]
    puv = matice[radek1][pozice] 
    if(matice2 == []):
        if((puv > 0 and nas >0) or (nas<0 and puv <0)):
            for i in range(len(matice[radek1])):
                matice[radek2][i] -= nas* matice[radek1][i]
        if(nas<0 and puv <0):
            for i in range(len(matice[radek1])):
                matice[radek2][i] += nas* matice[radek1][i]
        if(nas>0 and puv <0):
            for i in range(len(matice[radek1])):
                matice[radek2][i] += nas* matice[radek1][i]
                
        if(puv > 0 and nas <0):
            for i in range(len(matice[radek1])):
                matice[radek2][i] -= nas* matice[radek1][i]
    else:
        if((puv > 0 and nas >0) or (nas<0 and puv <0)):
            for i in range(len(matice[radek1])):
                matice[radek2][i] -= nas* matice[radek1][i]
                matice2[radek2][i] -= nas* matice2[radek1][i]
        if(nas<0 and puv <0):
            for i in range(len(matice[radek1])):
                matice[radek2][i] += nas* matice[radek1][i]
                matice2[radek2][i] += nas* matice2[radek1][i]
        if(nas>0 and puv <0):
            for i in range(len(matice[radek1])):
                matice[radek2][i] += nas* matice[radek1][i]
                matice2[radek2][i]+=  nas* matice2[radek1][i]
                
        if(puv > 0 and nas <0):
            for i in range(len(matice[radek1])):
                matice[radek2][i] -=  nas* matice[radek1][i]
                matice2[radek2][i] -=  nas* matice2[radek1][i]
        
            

     
#vraci pocet scitani nutnych pro vynulovani daneho sloupce(pozice), startovaci
#pozice zacina na zadanem radku

def pocet_scitani(matice,radek,pozice):
    pocet = 0
    pruchod = 0
    while(True):
        if((radek) == len(matice) and pruchod!=0):#nezacal jsem na konci matice a jsem na poslednim radku
            a = najdi_nenul_cis(matice, radek, pozice)
            if(a[1] != -1):
                pocet+=1
            break
        elif(radek == len(matice) and pruchod ==0): # zacal jsem na konci matice
            break
        else:             #hledej pod zadanym radkem nenul cisla a rekni kolik si jich nasel
            radek +=1 
            a = najdi_nenul_cis(matice,radek, pozice)
            if(a[1] != -1):
                pocet+=1
                radek = a[1]
            pruchod +=1
            
    return pocet        
        
#klasicke maticove nasobeni
def matnasob(mat1,mat2):
    vysl =[]
    if(len(mat1[0])==len(mat2)):
        soucet = 0
        prom = []
        for i in range(len(mat1)):
            for j in range(len(mat1)):
                for k in range(len(mat2)):
                    soucet += (mat1[i][k] * mat2[k][j])
                prom.append(round(soucet,2))#zaokrouhleni kvuli zaokr. chybe pocitace
                soucet = 0    
            vysl.append(prom)
            prom = []
    return vysl    

#protoceni matice kvuli zpetnemu chodu Gaussovy eliminace
#vezme prvni radek a vymeni ho z poslednim, vezme 2 radek a vymeni ho z predposl ....

#pote vezme 1. sloupec a vymeni ho z poslednim sloupcem, atd. 
def protoc(matice):
    menic = []
    inv= []
    for i in range(len(matice)):
        menic = matice[i]
        inv.append(menic[::-1])
    inv = inv[::-1]
    return inv

#odstraneni nulovych radku
def odstran_nul_radky(matice):
    for i in range(len(matice)):
        x = True
        for j in range(len(matice[i])):
            if(matice[i][j] != 0):
               break
            if(matice[i][j] == 0 and j == len(matice[i])):
                del matice[i]
 #Gaussova eliminace           
def Gauss(leva, volmat = []):#volitelna matice kvuli sparovani s inverzni
    global jeregular
    if(volmat == []):
        prava = jednotkova(len(leva))  #rozdeleni na pravou a levou stranu 
                                #(jako prava a leva strana matice rozsirene o pravou stranu)
    else:
        prava = volmat
    radek = 0
    sloup = 0 #start pozice
    while(True):
        hledac = najdi_nenul_cis(leva,radek,sloup) #najdi mi ve danem sloupci nenul cislo -> vraci hodnotu a index nenul cisla
        if(hledac[1] != -1): #pokud jsi nasel nenul cislo
            vydel(prava,hledac[1],leva[hledac[1]][sloup])#vydel radek cislem co jsi nasel
            vydel(leva,hledac[1],leva[hledac[1]][sloup])
            prohod(prava,radek,hledac[1])#prohod radek na ktery je nastavena promenna radek a radek na kterem jsi nasel nenul cislo
            prohod(leva,radek,hledac[1])
            a = pocet_scitani(leva,radek,sloup)#rekni mi kolik je nutnych scitani radku aby jsi pod nalezenym cislem vynuloval sloupec
            #print(a)
            #print()
            for i in range(a):
                hledac = najdi_nenul_cis(leva, radek +i + 1, sloup)# najdi pod radkem s nalezenym cislem nenul radek v danem sloupci
                nuluj(leva,radek,hledac[1],sloup,prava)#vynuluj ho
                #nuluj(prava,radek,hledac[1],sloup)
            #print("leva")
            #vypis(leva)
            #print("prava")
            #vypis(prava)
            #print()
        elif(hledac[1] == -1 and len(leva) != sloup):#kdyz je cely sloupec nulovy, pak matice neni regularni
            while(len(leva) != sloup+1):#osetreni situace, kdy je nulovy cely posledni radek, mozna zbytecne
                sloup +=1
                hledac = najdi_nenul_cis(leva,radek,sloup)
                if(hledac[1] != -1):
                    break
            
            #print("neni reg")
            jeregular = False
            break
        if(len(leva) == sloup):#dosel jsi nakonec a vsechny sloupce nenulove a na kazdem radku 1 cislo
            #print("je reg")   #pak je matice regularni a existuje k ni inverzni matice
            #vypis(prava)
            #vypis(leva)
            #print()
            jeregular = True
            return prava
        sloup+=1
        radek+=1
        
#zpetna Gaussova eliminace        
def Gauss_zpet(leva, prava = []):#volitelna prava strana pro hledani inverz mat
    if(jeregular == True):
        if(prava == []):
            vysl = jednotkova(len(leva)) #
        else:
            vysl = copy.deepcopy(prava)#pro nalezeni inv. matice, musi prava projit Gauss elim v predchoz funkci
        vysl = (protoc(vysl)) #protoceni cele matice kvuli aplikaci jiz naprogram. Gauss elim
        leva = protoc(leva)
        vysl = (Gauss(leva,vysl))  #zpetne protoceni matice
        vysl = protoc(vysl)
        #inv = protoc(leva)
        return vysl
    else:
        return []

    
"""    
puv = vytvor_matici(4,4)
pokus = copy.deepcopy(puv)
print("puv mat")
vypis(puv)     
inv = Gauss(pokus)
print("prava po gauss")
vypis(inv)
poc = Gauss_zpet(pokus, inv)
print("vysl")
vypis(poc)
print("puv")
vypis(puv)

#print(jeregular)
a = copy.deepcopy(poc)
b = copy.deepcopy(puv)
overeni = matnasob(a,b)
vypis(overeni)
"""

konec = True
zadani = 0
m = 2
n = 2
uziv_mat = []

while (True):
    zadani = int(input("zadej 1 pro zadani vlastni matice, zadej 0 pro nahodnou matici: "))
    if (zadani == 1):
        zad_radky = 0
        radek = []
        uziv_mat = []
        chyba = False
        nul_mat = True
        m = int(input("zadej m rozmer matice (m*n): "))
        n = int(input("zadej n rozmer matice (m*n): "))
        while(zad_radky < m ):
            radek = (input("zadej radek matice ve forme 1,2,3,4...: ")).split(",")
            for i in range(len(radek)):
                radek[i] = int(radek[i])
                if(radek[i] != 0):
                    nul_mat = False
            if(len(radek) != n):
                chyba = True
            uziv_mat.append(radek)
            radek = []
            zad_radky+=1
        if(chyba):
            print("spatne zadano")
        elif(m != n or nul_mat == True):
            print("matice neni regularni, neexistuje inv. mat.")
        else:
            puv = copy.deepcopy(uziv_mat)
            inv = Gauss(uziv_mat)
            if(jeregular == True):
                print("je regularni : " , jeregular)
                print()
                vysl = Gauss_zpet(uziv_mat, inv)
                print("inv. mat k zadane mat:")
                vypis(vysl)
                print()
                print("puvodni mat: ")
                vypis(puv)
                print()
                print("zkouska vynasobenim: ")
                a = copy.deepcopy(vysl)
                b = copy.deepcopy(puv)
                overeni = matnasob(a,b)
                vypis(overeni)
                
            else:
                print("je regularni : " , jeregular)
                print("upravena matice: ")
                print()
                vypis(inv)
        print("-------------")
        konec = int(input("zadej 1 pro konec, 0 pro pokracovani: "))
        if(konec == True):
            break
    else:
        m = int(input("zadej m rozmer matice (m*n): "))
        n = int(input("zadej n rozmer matice (m*n): "))
        if(m != n ):
            print("matice neni regularni, neexistuje inv. mat.")
        else:
            uziv_mat = vytvor_matici(m,n)
            puv = copy.deepcopy(uziv_mat)
            inv = Gauss(uziv_mat)
            if(jeregular == True):
                print("je regularni : " , jeregular)
                vysl = Gauss_zpet(uziv_mat, inv)
                print()
                print("inv. mat k zadane mat:")
                vypis(vysl)
                print()
                print("puvodni mat: ")
                vypis(puv)
                print()
                print("zkouska vynasobenim: ")
                a = copy.deepcopy(vysl)
                b = copy.deepcopy(puv)
                overeni = matnasob(a,b)
                vypis(overeni)
                
            else:
                print("je regularni : " , jeregular)
                print("upravena matice: ")
                print()
                vypis(inv)
        print("-------------")
        konec = int(input("zadej 1 pro konec, 0 pro pokracovani:"))
        if(konec == True):
            break
            
        
                
            
            
            
        
        
        
    
    
    
    




