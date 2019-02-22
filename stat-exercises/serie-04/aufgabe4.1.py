#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.stats import norm
from math import sqrt

# a)
mean_x = 40
mean_y = 85
sd_x = 15
sd_y = 18

e_x_plus_2y = mean_x + 2 * mean_y
print('E(X+2Y)={:d}'.format(e_x_plus_2y))

var_x_plus_2y = sd_x**2 +  (2 * sd_y) ** 2
print('Var(X+2Y)={:d}'.format(var_x_plus_2y))

# Var(X)=E(X²)-(E(X))² <=> E(X²)=Var(X)+(E(X))²
e_x_square = sd_x**2 + mean_x**2
print('E(X²)={:d}'.format(e_x_square))

# b)
mean_x = 1000
mean_y = 500
sd_x = 0.02
sd_y = 0.01

# E(U)=E(2X+2Y)
e_u = 2 * mean_x + 2 * mean_y
print('E(U)={:d}mm'.format(e_u))

# U=2X+2Y, Var(U)=Var(2X)+Var(2Y)
sd_u = sqrt(4 * sd_x ** 2 + 4 * sd_y ** 2)
print('σu={:.4f}mm'.format(sd_u))
