import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import plotly.graph_objects as go
import seaborn as sns

  
  
  
# assigning x and y coordinates  
sns.set_style("whitegrid")
x1= [43.12,42.68,42.73,41.94,43.38,42.51,43.27]
x2 = [57.91,58.4,58.98,58.91,57.76,56.60,57.55]
x3 = [124.84,129.81,127.91,127.22,126.13]

#plt.subplot(1,3,1)
fig, ax = plt.subplots(nrows = 1,ncols= 3)
plt.subplots_adjust(wspace = 0.7)
ax[0].set_xlabel("průměr [mm]",fontsize=11)
plt.grid(True)
ax[0].set_ylabel("četnost",fontsize = 11)
ax[0].hist(x1,14)


ax[1].set_xlabel("výška [mm]",fontsize=11)
plt.grid(True)
ax[1].set_ylabel("četnost",fontsize = 11)
ax[1].hist(x2,14,color = "purple")



ax[2].set_xlabel("hmotnost [g]",fontsize=11)
plt.grid(True)
ax[2].set_ylabel("četnost",fontsize = 11)
ax[2].hist(x3,14,color = "green")
ax[2].set_xticks([124,126,128,130])
ax[1].set_xticks([57,58,59])
ax[0].set_xticks([42,42.75,43.5])
ax[2].set_yticks([0.5,1])
ax[1].set_yticks([1,2])
ax[0].set_yticks([1,2])
plt.suptitle("Histogramy naměřených hodnot" , fontsize = 14)
plt.savefig("hustoty_ZFM.eps",format="eps")
plt.savefig("hustoty_ZFM.pdf",format = "pdf")
plt.show()
