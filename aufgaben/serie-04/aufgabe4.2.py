#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

for n in [2, 5, 10, 100]:
    m = 500
    ran = np.array(norm.rvs(size=n*m))
    sim = ran.reshape((n, m))

    # a)
    plt.plot(sim)
    plt.show()

    # b)
    plt.hist(sim.T, bins=20, density=True, edgecolor='black', facecolor='white')
    x = np.linspace(-4, 4, num=100)
    y = norm.pdf(x)
    plt.plot(x, y)
    plt.title('Histogram sim')
    plt.show()

    sim_mean = sim.mean(axis=0)
    plt.hist(sim_mean, density=True, edgecolor='black', facecolor='white')
    x = np.linspace(-4, 4, num=100)
    y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))
    plt.plot(x, y)
    plt.title('Histogram sim_mean')
    plt.show()
