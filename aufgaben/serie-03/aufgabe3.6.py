#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.stats import norm

exp = 0.2508
sd = 0.0005

# a)
a = norm.cdf(x=0.25-0.0015, loc=exp, scale=sd)
b = norm.cdf(x=0.25+0.0015, loc=exp, scale=sd)
print('P(0.25±0.0015)={:.3f}'.format(b-a))

# b)
exp = 0.25
a = norm.cdf(x=0.25-0.0015, loc=exp, scale=sd)
b = norm.cdf(x=0.25+0.0015, loc=exp, scale=sd)
print('P(0.25±0.0015)={:.3f}'.format(b-a))
