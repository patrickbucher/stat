#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
from math import sqrt

n_mice = 54
n_groups = 3
dose_high = 10.2
dose_medium = 1.2
dose_low = 0.3

iron = pd.read_table('./iron.dat', sep=' ', index_col=False)

# a)
plt.subplot(1, 2, 1)
iron.plot(kind='box', ax=plt.gca())
plt.ylabel('iron')
# Je kleiner die Dosis, desto grösser fällt die Streuung aus.

# b)
plt.subplot(1, 2, 2)
np.log(iron).plot(kind='box', ax=plt.gca())
plt.ylabel('log(iron)')
# Durch das Logarithmieren verschwinden die Ausreisser. Die Streuung der
# Gruppen gleicht sich einander an.

plt.tight_layout()
plt.show()

# c)
plt.subplot(1, 2, 1)
st.probplot(iron['medium'], plot=plt)
plt.ylabel('iron["medium"]')

plt.subplot(1, 2, 2)
st.probplot(np.log(iron['medium']), plot=plt)
plt.ylabel('log(iron["medium"])')
plt.show()
# Die Normalverteilung passt besser auf den logarithmierten Plot.

# d)
mean = iron['medium'].mean()
var = iron['medium'].var()
p = 1 - st.norm.cdf(x=10, loc=mean, scale=sqrt(var))
print('P(X<10)=1-P(X≤10)={:.4f}'.format(p))

# e)
mean = np.log(iron['medium']).mean()
var = np.log(iron['medium']).var()
p = 1 - st.norm.cdf(x=np.log(10), loc=mean, scale=sqrt(var))
print('P(X<log(10))=1-P(X≤log(10))={:.4f}'.format(p))
