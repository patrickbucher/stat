#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scipy.stats import norm
import numpy as np
from math import sqrt

a = [79.98, 80.04, 80.02, 80.04, 80.03, 80.03, 80.04, 79.97, 80.05, 80.03,
     80.02, 80.00, 80.02]
b = [80.02, 79.94, 79.98, 79.97, 79.97, 80.03, 79.95, 80.03, 79.95, 79.97]

# a)
mean_a = np.mean(a)
mean_b = np.mean(b)
se_a = np.std(a) / sqrt(len(a))
se_b = np.std(b) / sqrt(len(b))
print('μa={:.4f}'.format(mean_a))
print('σa={:.4f}'.format(se_a))
print('μb={:.4f}'.format(mean_b))
print('σb={:.4f}'.format(se_b))

print('Methode A: ({:.3f}±{:.3f})cal/g'.format(mean_a, se_a))
print('Methode B: ({:.3f}±{:.3f})cal/g'.format(mean_b, se_b))

# b)
ser_a = se_a / mean_a
ser_b = se_b / mean_b
print('Methode A: {:.3f}cal/g ±{:.3f}%'.format(mean_a, ser_a*100))
print('Methode B: {:.3f}cal/g ±{:.3f}%'.format(mean_b, ser_b*100))
