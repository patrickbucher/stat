#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.stats import norm

exp = 32
sd = 6

# b)
p_max_40ppb = norm.cdf(x=40, loc=exp, scale=sd)
print('P(X <= 40ppb)={:.3f}'.format(p_max_40ppb))

p_max_40ppb= norm.cdf(x=(40-exp)/sd)
print('P(Z <= (40-32)/6)={:.3f}'.format(p_max_40ppb))

# c)
p_max_27ppb = norm.cdf(x=27, loc=exp, scale=sd)
print('P(X <= 27ppb)={:.3f}'.format(p_max_27ppb))

p_max_27ppb = norm.cdf(x=((27-exp)/sd))
print('P(Z <= (27-32)/6)={:.3f}'.format(p_max_27ppb))

# d)
p = 0.975
c_975 = norm.ppf(q=p, loc=exp, scale=sd)
print('P(X < {:.3f})={}'.format(c_975, p))

# e)
p = 0.1
c_10 = norm.ppf(q=p, loc=exp, scale=sd)
print('P(X < {:.3f})={}'.format(c_10, p))

# f)
p_38ppb = norm.cdf(x=38, loc=exp, scale=sd)
p_26ppb = norm.cdf(x=26, loc=exp, scale=sd)
print('P(26 <= X <= 38)={:.3f}'.format(p_38ppb-p_26ppb))
p_38ppb = norm.cdf(x=(38-exp)/sd)
p_26ppb = norm.cdf(x=(26-exp)/sd)
print('P(26 <= X <= 38)={:.3f}'.format(p_38ppb-p_26ppb))
