#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.stats import norm

exp = 0
sd = 0.45
threshold = 0.9

# a)
# P(N > 0.9)
# N(0, 0.45²)
false_1 = 1 - norm.cdf(x=threshold, loc=exp, scale=sd)
print('P(N > {:.1f})={:.3f}'.format(threshold, false_1))

false_1 = 1 - norm.cdf(x=(threshold-exp)/sd)
print('P(N > {:.1f})={:.3f}'.format(threshold, false_1))

# b)
# P(-c < N) = 0.005
# P(N < c) = 0.995
c_neg = norm.ppf(q=0.005, loc=0, scale=sd)
print('[{:.3f},{:.3f}]'.format(c_neg, c_neg * -1))

# c)
# S ~ N(1.8, 0.45²)
nd_1 = norm.cdf(x=threshold, loc=1.8, scale=sd)
print('P(S < {:.1f})={:.3f}'.format(0.9, nd_1))
