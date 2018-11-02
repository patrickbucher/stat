#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scipy.stats as st
from math import exp, factorial

total_mins = 120
total_fish = 15

# a)
mean_time = total_mins/total_fish
p = 1 - (1 - exp(-12/mean_time))
print('P(T>12)=1-P(T≤12)={:.4f}'.format(p))

# b)
phase_mins = 12
mean_fish = total_fish/total_mins
phase_fish = mean_fish * phase_mins
x = 2
t = exp(-phase_fish) * phase_fish**2/factorial(x)
print('P(X=2)={:.4f}'.format(t))
