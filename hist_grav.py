import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import plotly.graph_objects as go
import seaborn as sns
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

cas4 = [0.236,0.240,0.238,0.240,0.236,0.248,0.244,0.240,0.238,0.244]
plt.hist(cas4,10)
plt.grid(True,axis = "x")

#set_xticks(range(0.224,0.256,4))


 
sns.set_style("whitegrid")





plt.xlabel("čas [s]",fontsize=11)
plt.ylabel("četnost",fontsize = 11)
plt.suptitle("Histogram naměřených hodnot" , fontsize = 14)
plt.savefig("grav_ZFM.eps",format="eps")
plt.savefig("grav_ZFM.pdf",format = "pdf")
plt.show()
