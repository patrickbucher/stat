#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.stats import uniform
import numpy as np
from math import sqrt

def hypot(x, y):
    return sqrt(x*x + y*y)

sizes = [10, 100, 1000, 10**4, 10**5, 10**6]

for size in sizes:
    x = uniform.rvs(size=size, loc=-1, scale=2)
    y = uniform.rvs(size=size, loc=-1, scale=2)
    n_in = 0
    n_out = 0
    for i in range(1, size):
        dist = hypot(x[i], y[i])
        if dist > 1.0:
            n_out += 1
        else:
            n_in += 1
    pi = n_in / n_out
    print('n = {:8d}, Pi = {:.5f}'.format(size, pi))
