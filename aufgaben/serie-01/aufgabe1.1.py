#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

# a)
print('a) read the data')
data = pd.read_csv('child.csv', sep=',', index_col=0)

# b)
print('\nb) display the shape:', data.shape)

# c)
print('\nc) describe the data:\n', data.describe())

# d)
print('\nd) Which countries are in the set?')
for i in data.index:
    if i == 'China':
        print('- Entry for China exists')
    elif i == 'Netherlands':
        print('- Entry for the Netherlands exists')

# e)
print('\ne) Top 5 countries in terms of Drunkenness')
drunk = data.sort_values(by='Drunkenness', ascending=False)
for i in range(0,5):
    print(drunk.index[i], drunk['Drunkenness'][i],
            '(highest percentage)' if i == 0 else '')

# f)
print('\nf) Lowest child mortality')
lowest_child_mortality = data.nsmallest(1, 'Infant.mortality')
print(lowest_child_mortality.index[0],
        lowest_child_mortality['Infant.mortality'][0])

# g)
print('\ng) Under-average physical activity')
col = 'Physical.activity'
low_physical_activity = data.loc[data[col] < data[col].mean()]
low_physical_activity = low_physical_activity.sort_values(by=col, ascending=True)
for i in low_physical_activity.index:
    print(i, low_physical_activity[col][i])
