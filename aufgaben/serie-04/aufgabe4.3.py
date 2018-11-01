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
print(prob_sample_mean_below_95)
