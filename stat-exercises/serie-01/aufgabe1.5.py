#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

geysir = pd.read_table('geysir.csv', sep=' ', index_col=0)

# a) Zeitspanne
plt.subplot(221)
geysir['Zeitspanne'].plot(kind='hist', edgecolor='black')
plt.xlabel('10 Klassen')

plt.subplot(222)
geysir['Zeitspanne'].plot(kind='hist', bins=20, edgecolor='black')
plt.xlabel('20 Klassen')

plt.subplot(223)
geysir['Zeitspanne'].plot(kind='hist',
        bins=np.arange(41, 107, 11),
        edgecolor='black')
plt.xlabel('Klassengrenten 41, 52, 63, 74, 85, 96')

plt.show()

# Was fällt auf?
# - Mit unterschiedlicher Balkenanzahl erscheinen unterschiedliche Trends.
# - Mit vielen Balken fluktuieren die benachbarten Klassen stärker.
# - Bei vielen Balken gibt es eher Klassen ohne Messwerte.

# b) Eruptionsdauer
plt.subplot(221)
geysir['Eruptionsdauer'].plot(kind='hist', bins=10, edgecolor='black')
plt.xlabel('10 Klassen')

plt.subplot(222)
geysir['Eruptionsdauer'].plot(kind='hist', bins=20, edgecolor='black')
plt.xlabel('20 Klassen')

plt.subplot(223)
geysir['Eruptionsdauer'].plot(kind='hist', bins=6, edgecolor='black')
plt.xlabel('30 Klassen')

plt.show()

# Was fällt auf?
# - Im Gegensatz zu den Zeitspannen ist bei der Eruptionsdauer bei allen
#   Diagrammen der gleiche Trend erkennbar.

# c) Verteilungsfunktion
geysir['Eruptionsdauer'].plot(kind='hist',
        density=True,
        cumulative=True)
plt.show()

eruption = geysir['Eruptionsdauer']
max_2min = eruption <= 2
n_max_2min = eruption[max_2min].count()
n = eruption.count()
print('Eruptionsdauer <= 2min: {:.2f}%'.format(n_max_2min / n * 100))

min_top60percent = eruption.quantile([0.6]).values[0]
print('Mindestdauer der 60% Top-Eruptionsdauern: {} min.'.format(min_top60percent))
