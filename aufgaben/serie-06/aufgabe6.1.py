#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
import numpy as np
from pandas import Series
from scipy.stats import norm

# Step 1: Model N(70, 1.5²)
mean = 70 # cl
sd = 1.5 # cl

# Step 2: Null Hypothesis: follows distribution!

# Step 3: Test Statistics
measurements = Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])
z = (measurements.mean() - mean) / (sd / sqrt(measurements.size))
print('Z={:.4f}'.format(z))

# Step 4: 
a = 0.05

# Step 5:
val = norm.ppf(q=0.05, loc=mean, scale=sd/sqrt(measurements.size))
print('val={:.4f}'.format(val))
stderr = sd/sqrt(measurements.size)
print(stderr)
print((val-mean)/stderr)
print(norm.ppf(q=0.05)) # Anzahl Standardabweichungen
print(norm.cdf(x=val, loc=mean, scale=sd))

# Step 6: Testentscheid
print(measurements.mean())

# standardisiert
print((measurements.mean()-70)/(measurements.std()/np.sqrt(measurements.size)))
