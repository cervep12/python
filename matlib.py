# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:22:49 2020

@author: Petr
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
np.random.seed(123)
r = np.random.rand(2,100)+1.5
np.random.seed(321)
s = np.random.rand(2,100)+2
np.random.seed(456)
a = np.random.rand(2,100)+2.5
np.random.seed(789)
b = np.random.rand(2,100)+2
"""
np.random.seed(100)
x = list(range(30))
y = x + np.random.rand(30)-8
fit = np.polyfit(x,y,3)
plt.grid()
yfit = [n*fit[0] for n in x] + fit[1]
plt.scatter(x,y)
plt.plot(yfit,"black")


plt.show()