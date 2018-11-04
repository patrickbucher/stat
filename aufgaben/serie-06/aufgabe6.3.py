#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scipy.stats import norm, t
from math import sqrt

sample_size = 16
sample_mean = 204.2
population_mean = 200
significance_level = 0.05

# a)
population_sd = 10

# 1. model: normal distribution
# 2. null hypothesis: population_mean = sample_mean
# 3. test statistics: z-value
# 4. significance level: 0.05
# 5. rejection zone: [z,∞) (sample mean *significantly* over population mean)
# 6. decision
p = 1 - norm.cdf(x=sample_mean, loc=population_mean, scale=population_sd/sqrt(sample_size))
print('a) z test: p={:.4f}'.format(p))
if p < significance_level:
    print('reject null hypotesis')

# b)
real_population_mean = 205
p = 1 - norm.cdf(x=population_mean, loc=real_population_mean, scale=population_sd/sqrt(sample_size))
print('b) probability={:.1f}%'.format(p * 100))

# c)
real_population_mean = 200
p = 1 - norm.cdf(x=population_mean, loc=real_population_mean, scale=population_sd/sqrt(sample_size))
print('c) probability={:.1f}%'.format(p * 100))

# d)
sample_sd = 10
p = 1 - t.cdf(x=sample_mean, df=sample_size-1, loc=population_mean, scale=sample_sd/sqrt(sample_size))
print('d) t test: p={:.4f}'.format(p))

# e) Die einzelnen Messwerte sind vielleicht nicht unabhängig voneinander, da
# es sich nicht bei jeder Messung um komplett anderes Wasser handeln könnte.
