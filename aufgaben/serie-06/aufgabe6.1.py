#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
import numpy as np
from pandas import Series
from scipy.stats import norm

# Step 1: model N(70, 1.5²)
mean = 70 # cl
sd = 1.5 # cl

# Step 2: null hypothesis: bottle filling follows model

# Step 3: test statistics
measurements = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
z = (measurements.mean() - mean) / (sd / sqrt(measurements.size))
print('Z={:.4f}'.format(z))

# Step 4: define significance level
a = 0.05

# Step 5: rejection area for test statistics
# ppf: percentile point function
val = norm.ppf(q=0.05, loc=mean, scale=sd/sqrt(measurements.size))
print('val={:.4f}'.format(val)) # at which value is the 5th percentile?

stderr = sd/sqrt(measurements.size)
print('standard error={:.4f}'.format(stderr))

print('standard deviations: {:.4f}'.format((val-mean)/stderr))
print('standard deviations: {:.4f}'.format(norm.ppf(q=0.05)))
print('p-value: {:.4f}'.format(norm.cdf(x=val, loc=mean, scale=sd)))

# Step 6: decide
print('null hypothesis mean={:.4f}, measurement mean={:.4f}'.format(mean,
    measurements.mean()))

# standardized
print('standardized={:.4f}'.format(
    (measurements.mean()-70)/(measurements.std()/np.sqrt(measurements.size))))
