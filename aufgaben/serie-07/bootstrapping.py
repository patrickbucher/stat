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
