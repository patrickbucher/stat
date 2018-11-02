#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from pandas import Series, DataFrame
from math import sqrt

values = np.array([0, 10, 11])

# a)
sim = Series(np.random.choice(values, size=1000, replace=True))
plt.subplot(4, 2, 1)
sim.hist(bins=[0, 1, 10, 11, 12], edgecolor='black')
plt.title('Original')
plt.subplot(4, 2, 2)
st.probplot(sim, plot=plt)
plt.title('Normal Q-Q Plot')

# b)
n = 5
sim = np.random.choice(values, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim, (n, 1000)))
sim_mean = sim.mean()
plt.subplot(4, 2, 3)
sim_mean.hist(edgecolor='black')
plt.title('Mittelwerte von 5 Beobachtungen')
plt.subplot(4, 2, 4)
st.probplot(sim_mean, plot=plt)
plt.title('Normal Q-Q Plot')

# c)
i = 5
ns = [10, 200]
for n in ns:
    sim = np.random.choice(values, size=n*1000, replace=True)
    sim = DataFrame(np.reshape(sim, (n, 1000)))
    sim_mean = sim.mean()
    plt.subplot(4, 2, i)
    sim_mean.hist(edgecolor='black')
    plt.title('Mittelwerte von {} Beobachtungen'.format(n))
    i += 1
    plt.subplot(4, 2, i)
    st.probplot(sim_mean, plot=plt)
    plt.title('Normal Q-Q Plot')
    i += 1

plt.tight_layout()
plt.show()

# d)
n = 200
e_x = values.sum() / values.size
print('Berechnung:')
print('E[Xn]={}'.format(e_x))
n_x = len(values)
var_x = ((values[0]-e_x)**2/n_x + (values[1]-e_x)**2/n_x + (values[2]-e_x)**2/n_x)/n
print('Var[Xn]={:.4f}'.format(var_x))
print('σ[Xn]={:.4f}'.format(sqrt(var_x)))

print('\nSimulation')
sim = np.random.choice(values, size=n*1000, replace=True)
sim = DataFrame(np.reshape(sim, (n, 1000)))
sim_mean = sim.mean()
print('E[Xn]={}'.format(sim_mean.mean()))
print('Var[Xn]={:.4f}'.format(sim_mean.std()**2))
print('σ[Xn]={:.4f}'.format(sim_mean.std()))
