#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

# a)
fuel = pd.read_table('fuel.csv', sep=',', index_col=0)

# b)
print('\nb) fifth entry')
print(fuel.loc[5])

# c)
print('\nc) entries 1 to 5')
print(fuel.loc[1:5])

# d)
print('\nd) mean mileage per gallon')
print(fuel["mpg"].mean())

# e)
print('\ne) mean mileage of cars 7 to 22')
print(fuel["mpg"][7:22].mean())

# f)
l_per_gallon = 3.7891
km_per_mile = 1.6093
t_kml = pd.Series([e * (km_per_mile/l_per_gallon) for e in fuel["mpg"]])

kilograms_per_pound = 0.45359
t_kg = pd.Series([e * kilograms_per_pound for e in fuel["weight"]])

# g)
print('\ng) mean km/l and kg')
print(t_kml.mean(), t_kg.mean())
