# Pandas

Import pandas using the `pd` acronym:

```python
import pandas as pd
```

## Series

Creating a series:

```python
age = pd.Series([87, 61, 34, 31, 26, 2],
        name='age')
```

Produces the series with the given values and an index (_axis labels_):

    0   87
    1   61
    2   34
    3   31
    4   26
    5    2
    Name: age, dtype: int64

Inspecting the index of a series:

```python
age.index
```

Output:

    RangeIndex(start=0, stop=6, step=1)

Create a series with a string-based index:

```python
age = pd.Series([87, 61, 34, 31, 26, 2],
        index=['grandpa', 'mom', 'sister', 'I', 'wife', 'nephew'],
        name='age')

```

Produces:

    grandpa     87
    mom         61
    sister      34
    I           31
    wife        26
    nephew       2
    Name: age, dtype: int64

Getting the number of entries:

```python
age.count() # 6
```

Calculating the mean and median:

```python
age.mean() # 40.166...
age.median() # 32.5
```

Creating a mask -- a boolean array denoting whether or not an entry fulfills a
condition:

```python
old_mask = age > age.median()
```

Produces:

    grandpa     True
    mom         True
    sister      True
    I          False
    wife       False
    nephew     False
    Name: age, dtype: bool

Use the mask to select matching entries:

```python
age[old_mask]
```

Produces:

    grandpa     87
    mom         61
    sister      34
    Name: age, dtype: int64
