#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.8, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

# a)
plt.subplot(221)
b, a = np.polyfit(x, y1, deg=1)
l = np.linspace(x.min(), x.max())
plt.plot(l, a+b*l, c='orange')
plt.scatter(x=x, y=y1)
# Linie verläuft ober- und unterhalb der Messpunkte.

plt.subplot(222)
b, a = np.polyfit(x, y2, deg=1)
plt.scatter(x=x, y=y2)
plt.plot(l, a+b*l, c='orange')
# Linie schneidet den konkaven Bogen.

plt.subplot(223)
b, a = np.polyfit(x, y3, deg=1)
plt.scatter(x=x, y=y3)
plt.plot(l, a+b*l, c='orange')
# Linie stark durch Ausreisser beeinflusst.

plt.subplot(224)
b, a = np.polyfit(x4, y4, deg=1)
l = np.linspace(x4.min(), x4.max())
plt.scatter(x=x4, y=y4)
plt.plot(l, a+b*l, c='orange')
# Linie durch zwei Punkte, wobei der erster das Mittel von vielen Messpunkten
# und der zweite ein einziger Messpunkt ist.

plt.show()

# b)

# TODO: what?

# c)
c1 = np.corrcoef(x, y1)[0][1]
c2 = np.corrcoef(x, y2)[0][1]
c3 = np.corrcoef(x, y3)[0][1]
c4 = np.corrcoef(x4, y4)[0][1]
print(c1, c2, c3, c4)

# Die Korrelationskoeffizienten sind praktisch überall gleich.
