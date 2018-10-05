#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

income = pd.read_table('income.txt', sep=' ')

# b)
b, a = np.polyfit(income['Educ'], income['Income2005'], deg=1)
print('y = {} + {}x'.format(b, a))
x = np.linspace(income['Income2005'].min(), income['Income2005'].max())

# a)
income.plot(kind='scatter',x='Educ', y='Income2005')
#plt.plot(x, a+b*x, c='orange')
plt.show()
income.plot(kind='scatter', x='AFQT', y='Income2005')
#plt.plot(x, a+b*x, c='orange')
plt.show()
