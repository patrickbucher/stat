#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.stats import norm
from math import sqrt

# a)
mean = 1
sd = 2
n = 50

e_S = n * mean 
var_S = n * sd**2
print('E(S)={}'.format(e_S))
print('Var(S)={}'.format(var_S))

e_X = e_S / n
var_X = 1/n**2 * n * sd**2
print('E(X)={}'.format(e_X))
print('Var(X)={}'.format(var_X))

# b)
p = (norm.cdf(x=2, loc=mean, scale=sd) -
    norm.cdf(x=0, loc=mean, scale=sd))
print('P(E[X1]-1≤X1≤E[X1]+1)={:.4f}'.format(p))

# c)
p = (norm.cdf(x=51, loc=e_S, scale=sqrt(var_S)) -
    norm.cdf(x=49, loc=e_S, scale=sqrt(var_S)))
print('P(E[Sn]-1≤Sn≤E[Sn]+1)={:.4f}'.format(p))

# d)
p = (norm.cdf(x=2, loc=e_X, scale=sqrt(var_X)) -
    norm.cdf(x=0, loc=e_X, scale=sqrt(var_X)))
print('P(E[Xn]-1≤Xn≤E[Xn]+1)={:.4f}'.format(p))
