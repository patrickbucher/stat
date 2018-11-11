#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
import numpy as np
from pandas import Series
from scipy.stats import norm, t

# Step 1: model N(70, 1.5²)
mean = 70 # cl
sample_sd = 1.96

# Step 2: null hypothesis: bottle filling follows model
# H0: population mean = sample mean = 70
# HA: population mean < sample mean = 70

# Step 3: test statistics
measurements = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
sample_mean = measurements.mean()
T = (sample_mean - mean) / (sample_sd / sqrt(measurements.size))
print('T={:.4f}'.format(T))

# Step 4: define significance level
a = 0.05

# Step 5: rejection area for test statistics
# ppf: percentile point function
val = t.ppf(q=a, df=measurements.size - 1, loc=mean, scale=sample_sd/sqrt(measurements.size))
print('5h percentile at {:.4f}'.format(val)) # at which value is the 5th percentile?
p = t.cdf(x=sample_mean, df=measurements.size - 1, loc=mean, scale=sample_sd/sqrt(measurements.size))
print('p={:.4f}'.format(p))

# Step 6: decision
# the p value is way bigger than 0.05: accept null hypothesis
