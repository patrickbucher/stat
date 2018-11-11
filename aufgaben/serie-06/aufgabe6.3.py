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
val = norm.ppf(q=1-significance_level, loc=population_mean, scale=population_sd/sqrt(sample_size))
print('5th percentile at: {:.4f}'.format(val))
p = 1 - norm.cdf(x=sample_mean, loc=population_mean, scale=population_sd/sqrt(sample_size))
print('a) z test: p={:.4f}'.format(p)) # a) z test: p=0.0465
if p < significance_level:
    print('reject null hypotesis')

# b)
real_population_mean = 205
p = 1 - norm.cdf(x=val, loc=real_population_mean, scale=population_sd/sqrt(sample_size))
print('b) probability={:.1f}%'.format(p * 100)) # b) probability=63.9%

# c)
x = (val - real_population_mean) / (population_sd / sqrt(sample_size))
print('x={:.4f}'.format(x))
p = 1 - norm.cdf(x=x)
print('c) probability={:.1f}%'.format(p * 100)) # c) probability=63.9%
p = 1 - norm.cdf(x=val, loc=real_population_mean, scale=population_sd/sqrt(sample_size))
print('c) probability={:.1f}%'.format(p * 100)) # c) probability=63.9%

# two ways of expressing the same:
# norm.cdf(x=(val-sample_mean)/stderr)
# norm.cdf(x=val, loc=sample_mean, scale=stderr)

# d)
sample_sd = 10
val = t.ppf(q=1-significance_level, df=sample_size-1, loc=population_mean, scale=sample_sd/sqrt(sample_size))
print('d) 95th percentile at: {:.4f}'.format(val))
p = 1 - t.cdf(x=sample_mean, df=sample_size-1, loc=population_mean, scale=sample_sd/sqrt(sample_size))
print('d) t test: p={:.4f}'.format(p)) # d) t test: p=0.0568

# e) Die einzelnen Messwerte sind vielleicht nicht unabhängig voneinander, da
# es sich nicht bei jeder Messung um komplett anderes Wasser handeln könnte.
