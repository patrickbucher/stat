#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

marks = pd.Series([4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 5.2, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1])
mean_orig = marks.mean()
median_orig = marks.median()

print('original: mean={:.2f}, median={:.2f}'.format(mean_orig, median_orig))

# a)
marks_sorted = marks.sort_values()
i_below_median = int(marks_sorted.count() / 2) - 1
i_above_median = int(marks_sorted.count() / 2) + 1
marks_sorted[i_below_median] = 1.0
marks_sorted[i_below_median - 1] = 1.0
marks_sorted[i_above_median] = 6.0
mean_fake = marks_sorted.mean()
median_fake = marks_sorted.median()

print('fake: mean={:.2f}, median={:.2f}'.format(mean_fake, median_fake))

# b)
plt.subplot(211)
marks.plot(kind='hist', cumulative=True, histtype='step', density=True, bins=8,
        edgecolor='black')

plt.subplot(212)
marks.plot(kind='box', title='Boxplot')
plt.show()
