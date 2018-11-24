#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import probplot

#x = pd.Series([30, 37, 36, 43, 42, 43, 43, 46, 41, 42])
x = np.array([30, 37, 36, 43, 42, 43, 43, 46, 41, 42])
sample_mean = x.mean()
print('sample={}, mean={:.3f}'.format(x, sample_mean))
n = x.size
np.random.seed(1)
xbar = x.mean()

nboot = 10000

tmpdata = np.random.choice(x, n*nboot, replace=True)
bsmean = tmpdata.mean()
print('data={}, mean={:.3f}'.format(tmpdata, bsmean))

# means of bootstrap samples
bssample = np.reshape(tmpdata, (n, nboot))
xbarstar = bssample.mean(axis=0)
print(np.sort(xbarstar))

# confidence interval using standard error
d = xbar - 2 * xbarstar.std(), xbar + 2 * xbarstar.std()
print('confidence interval: ', d)

# confidence interval
d = np.percentile(xbarstar, q=[2.5, 92.5])
print('confidence interval: ', d)

# plot
xbarstar = pd.Series(bssample.mean(axis=0))
plt.subplot(121)
xbarstar.plot(kind='hist', edgecolor='black')
plt.subplot(122)
probplot(xbarstar, plot=plt)
plt.show()

# TODO:
x = np.random.normal(loc=40, scale=5, size=100)
n = x.size
np.random.seed(4)
xbar = x.mean()
nboot = 20
bootstrap_samples = np.random.choice(x, n*nboot, replace=True)
bootstrap_sample_array = np.reshape(bootstrap_samples, (n, nboot))
xbarstar = bootstrap_sample_array.mean(axis=0)
deltastar = xbarstar - xbar
print('deltastar={}'.format(deltastar))
d = np.percentile(deltastar, q=[2.5, 97.5])
ci = xbar - [d[1], d[0]]
print('confidence interval: {}'.format(ci))

# TODO:
x = np.random.normal(loc=40, scale=5, size=100000)
measurement_array = np.reshape(x, (1000, 100))
print(measurement_array.shape)
print(measurement_array[1].size)
nboot = 1000
n = 100
k = 0
for i in range(0, 1000):
    x = measurement_array[i]
    xbar = x.mean()
    bootstrap_samples = np.random.choice(x, n*nboot, replace=True)
    bootstrap_sample_array = np.reshape(bootstrap_samples, (n, nboot))
    xbarstar = bootstrap_sample_array.mean(axis=0)
    deltastar = xbarstar - xbar
    d = np.percentile(deltastar, q=[2.5, 97.5])
    if xbar-d[0] >= 40 >= xbar-d[1]:
        k += 1
print('k={:d}'.format(k))

# TODO:
x = np.random.normal(loc=40, scale=100, size=10000)
measurement_array = np.reshape(x, (100, 100))
print(measurement_array.shape)
nboot = 10000
n = 100
for i in range(0, 100):
    y = measurement_array[i]
    xbar = y.mean()
    tmpdata = np.random.choice(y, n*nboot, replace=True)
    bootstrapsample = np.reshape(tmpdata, (n, nboot))
    xbarstar = bootstrapsample.mean(axis=0)
    deltastar = xbarstar - xbar
    d = np.percentile(deltastar, q=[2.5, 97.5])
    plt.plot([i, i], [xbar-d[1], xbar-d[0]])
    if (xbar-d[1] <= 40 <= xbar-d[0]) == False:
        plt.plot([i, i], [xbar-d[1], xbar-d[0]], c='black', linewidth=3)
plt.plot([-5, 105], [40,40])
plt.show()
