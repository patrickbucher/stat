#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

schlamm = pd.read_table('klaerschlamm.txt', sep=' ', index_col=0)
schlamm = schlamm.drop('Labor', 1)

# a)
print(schlamm.describe())
schlamm.plot(kind='box')
plt.show()

# b)
schlamm_centered = schlamm - schlamm.median()
schlamm_centered.T.plot(kind='box')
plt.show()
