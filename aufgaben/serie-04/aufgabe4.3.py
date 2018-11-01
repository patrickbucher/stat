#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.stats import norm
from math import sqrt

# a)
mean_population = 100
sd_population = 10
sample_size = 25

sd_sample = sd_population / sqrt(sample_size)
prob_sample_mean_below_95 = norm.cdf(x=95, loc=mean_population, scale=sd_sample)
print('P(X<95)={:.4f}'.format(prob_sample_mean_below_95))

# b)
sample_size = 40
mean_population = (4 + 6) / 2
var_population = ((6 - 4) ** 2) / 12
mean_x = mean_population
var_x = sqrt(var_population) / sqrt(sample_size)
print('μ={:.4f}, Var={:.4f}'.format(mean_x, var_x))
