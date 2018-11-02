#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

n_mice = 54
n_groups = 3
dose_high = 10.2
dose_medium = 1.2
dose_low = 0.3

iron = pd.read_table('./iron.dat', sep=' ', index_col=False)

# a)
iron.plot(kind='box')
plt.show()
