#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

# a)
i = 1
ns = [10, 20, 50, 100]
for n in ns:
    x = st.norm.rvs(size=n)
    plt.subplot(len(ns), 1, i)
    st.probplot(x, plot=plt)
    plt.title('n={}'.format(n))
    i += 1
plt.tight_layout()
plt.show()

# b)
dfs = [20, 7]
ns = [20, 100]
for df in dfs:
    i = 1
    for n in ns:
        x = st.t.rvs(size=n, df=df)
        plt.subplot(len(ns), 1, i)
        st.probplot(x, plot=plt)
        plt.title('n={}, df={}'.format(n, df))
        i += 1
    plt.tight_layout()
    plt.show()

# c)
ns = [20, 100]
dfs = [20, 1]
for df in dfs:
    i = 1
    for n in ns:
        x = st.chi2.rvs(size=n, df=df)
        plt.subplot(len(ns), 1, i)
        st.probplot(x, plot=plt)
        plt.title('n={}, df={}'.format(n, df))
        i += 1
    plt.tight_layout()
    plt.show()
