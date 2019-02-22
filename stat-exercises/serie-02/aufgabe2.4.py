#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# a)
hubble = pd.read_table('hubble.txt', sep=' ')
print(hubble.describe())

# b)
b1, b0 = np.polyfit(hubble['distance'], hubble['recession.velocity'], deg=1)
print('y = {} + {}x'.format(b1, b0))

# c)
c = hubble.corr().iloc[0,1]
print(c) # 0.79: Korrelation erkennbar
