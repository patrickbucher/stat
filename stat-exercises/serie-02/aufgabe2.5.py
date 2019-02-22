#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# a)
income = pd.read_table('income.txt', sep=' ')

# a/b)

income.plot(kind='scatter', x='Educ', y='Income2005')
b, a = np.polyfit(income['Educ'], income['Income2005'], deg=1)
print('y = {} + {}x'.format(b, a))
x = np.linspace(income['Educ'].min(), income['Educ'].max())
plt.plot(x, a+b*x, c='orange')
plt.show()

income.plot(kind='scatter', x='AFQT', y='Income2005')
b, a = np.polyfit(income['AFQT'], income['Income2005'], deg=1)
x = np.linspace(income['AFQT'].min(), income['AFQT'].max())
plt.plot(x, a+b*x, c='orange')
plt.show()

# c)
iq_income_corr = income.corr().iloc[0,2]
educ_income_corr = income.corr().iloc[0,1]
print('IQ/Income Correlation: {:.3f}'.format(iq_income_corr))
print('Education/Income Correlation: {:.3f}'.format(educ_income_corr))

# IQ/Income Correlation: 0.308 (very weak)
# Education/Income Correlation: 0.595 (weak)
