#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from math import sqrt

hectars = pd.Series([2.1,2.4,2.8,3.1,4.2,4.9,5.1,6.0,6.4,7.3,10.8,12.5,
    13.0,13.7,14.8,17.6,19.6, 23.0,25.0,35.2,39.6])

# a)
print('a) sum')
print(hectars.sum())
squared_hectars = pd.Series([e ** 2 for e in hectars])
print(squared_hectars.sum())

# b)
print('\nb) mean and standard deviation')
mean = hectars.sum() / hectars.count()
print(mean)
squared_differences = [(mean - e)**2 for e in hectars]
sum_squared_differences = 0.0
for d in squared_differences:
    sum_squared_differences += d
variance = sum_squared_differences / (len(squared_differences) - 1)
std = sqrt(variance)
print(std)

# NOTE check against pandas implementations:
# print(hectars.mean())
# print(hectars.std())

# c)
print('\nc) median')
sorted_hectars = hectars.sort_values()
if sorted_hectars.count() % 2 == 0:
    # even number of elements: mean of middle two
    i = int(sorted_hectars.count() / 2)
    j = i - 1
    median = (sorted_hectars.values[i] + sorted_hectars.values[j]) / 2
else:
    # odd number of elements: middle element
    median = sorted_hectars.values[int(sorted_hectars.count() / 2)]
print(np.round(median))

# NOTE check against pandas implementation:
print(np.round(hectars.median()))

# d)
print('\nd) mean, standard deviation, median, 75% quantile')
print(hectars.mean())
print(hectars.std())
print(hectars.median())
print(hectars.quantile([0.75]).values[0])

# e)
print('\ne) mean and standard deviation of standardized values')
standardized = pd.Series([(x - mean) / std for x in hectars])
print(standardized.mean()) # must be 0
print(standardized.std()) # must be 1
