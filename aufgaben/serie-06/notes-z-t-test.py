#!/usr/bin/env python3

from pandas import Series
from math import sqrt
from scipy.stats import norm, t

# z-Test: calculate p value (population_sd known)
population_mean = 50
population_sd   = 1
sample          = Series([49.5, 50.1, 48.9, 50.3, 49.1])

p = norm.cdf(x=sample.mean(), loc=population_mean, scale=population_sd/sqrt(sample.size))
print('z-Test: p={:4f}'.format(p))

# t-Test: calculate p value (population_sd unknown)
p = t.cdf(x=sample.mean(), df=sample.size-1, loc=population_mean, scale=sample.std()/sqrt(sample.size))
print('t-Test: p={:4f}'.format(p))
