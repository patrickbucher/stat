# Pandas

Pandas is a package built on top of NumPy, which offers powerful data
operations familiar to those of data bases and spreadsheets. The fundamental
data structures of Pandas are `Series`, `DataFrame` and `Index`. A `DataFrame`
is a multidimensional array with labeled rows and columns, which supports
heterogeneous and missing data—an issue often to be faced with in real-world
data sets.

Pandas is idiomatically imported as `pd`:

```python
>>> import pandas as pd
```

## Series

What NumPy's `ndarray` is to Python's list, Pandas `Series` is to Python's
dictionary: a fast and very powerful alternative. Whereas Python's dictionary
maps a set of _arbitrary keys_ to  a set of _arbitrary values_, Pandas `Series`
maps a set of _typed keys_ to a set of _typed values_. A `Series` is made up of
two sequences:

1. `values`: a NumPy array (`np.ndarray`)
2. `index`: a Pandas Index (`pd.Index`)

### Creation

A Pandas `Series` can be created from scalars, lists and dictionaries.

If a `Series` is generated from list, the indices (first column) for the values
(second column) are made up automatically, i.e. sequentially:

```python
>>> pd.Series([1, 2, 3])
0    1
1    2
2    3
dtype: int64
```

An list of indices can be explicitly provided using the `index` parameter. The
the lists of values and indices need to have the same length:

```python
>>> pd.Series([1, 2, 3], index=['a', 'b', 'c'])
a    1
b    2
c    3
dtype: int64
```

However, indices can be noncontiguous and nonsequential:

```python
>>> pd.Series([1, 2, 3], index=['Foo', 'Bar', 'Qux'])
Foo    1
Bar    2
Qux    3
dtype: int64
```

If a scalar value is used instead of list of values, the same value will be
repeated for the length of the `index` list:

```python
>>> pd.Series(42, index=[1, 2, 3])
1    42
2    42
3    42
dtype: int64
```

A `Series` can be created based on a dictionary with keys to be used as
indices:

```python
>>> pd.Series({'a': 1, 'b': 2, 'c': 3})
a    1
b    2
c    3
dtype: int64
```

An additional list of indices can be provided to further select values from the
dictionary by their keys, and to specify the order of entries:

```python
>>> pd.Series({'a': 1, 'b': 2, 'c': 3}, index=['c', 'a'])
c    3
a    1
dtype: int64
```

### Access: Indexing and Selection

The elements of a `Series` can be accessed using indexing and slicing:

```python
>>> s = pd.Series([1, 2, 3, 4, 5])
>>> s[0]
1

>>> s[4]
5

>>> s[1:4]
1    2
2    3
3    4
dtype: int64
```

If arbitrary (noncontiguous, nonsequential) indices are used, slicing is
possible because of the fixed order of indices, but the upper bound is also
included:

```python
>>> payroll = pd.Series({'Dilbert': 120000, 'Wally': 80000, 'Alice': 110000})
>>> payroll['Dilbert':'Wally']
Dilbert  120000
Wally     80000
dtype: int64
```

Even though a non-numeric is used, a `Series` can also be sliced using a
implicit index. Here, the upper bound is excluded:

```python
>>> payroll[0:2]
Dilbert    120000
Wally       80000
dtype: int64
```

The elements of a `Series` can also be accessed through the means of masking
and fancy indexing:

```python
>>> payroll[(payroll >= 100000) & (payroll <= 150000)]
Dilbert    120000
Alice      110000
dtype: int64

>>> payroll[['Alice', 'Dilbert']]
Alice      110000
Dilbert    120000
dtype: int64
```

Python's native dictionary expressions are also supported:

```python
>>> 'Dilbert' in payroll
True

>>> 'Asok' in payroll
False

>>> payroll.keys()
Index(['Dilbert', 'Wally', 'Alice'], dtype='object')

>>> list(payroll.items())
[('Dilbert', 120000), ('Wally', 80000), ('Alice', 110000)]

>>> payroll['Wally'] = 90000 # modify existing entry
>>> payroll['Asok']  = 12000 # add a new entry
```

### Explicit and Implicit Indexing

When using a explicit integer index, indexing operations make use of the
explicit indices (the actual index values provided), but slicing operations use
the implicit indices (the items ordinal numbers). This can be confusing:

```python
>>> ratings = pd.Series([2.3, 3.1, 3.9, 4.2, 4.8], index=[10, 20, 30, 40, 50])
>>> ratings[10] # explicit index
2.3

>>> ratings[1:3] # implicit index
20    3.1
30    3.9
dtype: float64
```

In order to reduce that confusion, a `Series` offers two attributes to access
the indices:

- `loc`: the explicit index
- `iloc`: the implicit index

```python
>>> ratings.loc[10]
2.3

>>> ratings.loc[10:30] # inclusive explicit indices from 10 to 30
10    2.3
20    3.1
30    3.9
dtype: float64


>>> ratings.iloc[0]
2.3

>>> ratings.iloc[0:3] # exclusive implicit indices from 0 to 3
10    2.3
20    3.1
30    3.9
dtype: float64
```

According to the [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
(«Explicit is better than implicit.»), slicing and indexing on `Series` using a
integer index should be done using the `loc` and `iloc` attributes,

## DataFrame

A Pandas `DataFrame` can be understood in terms of other data structures from
two perspectives:

1. As a generalization of a NumPy array of two dimensions, with row indices and
   column names being flexible.
    - NumPy arrays are indexed as `arr[row, column]`: row first, column second.
    - Pandas `DataFrame`s are indexed as `df[column][row]`: column first, row
      of the `Series` second.
2. As a specialization of a Python dictionary that maps a column name (key) to
   a `Series` of column data (value).

Generally speaking, a `DataFrame` is a sequence of `Series` sharing the index
value. Important attributes are:

- `columns`: returns an `Index` object (column names)
- `index`: returns the index labels (row names)

### Creation

A Pandas `DataFrame` can be created from `Series`, dictionaries and NumPy arrays.

If a single `Series` is provided, an optional column name for those values can
be defined in a list:

```python
>>> s = pd.Series([1, 2, 3])
>>> pd.DataFrme(s, columns=['values'])
   values
0       1
1       2
2       3
```

If a list of dictionaries is provided, each dictionary is mapped to a row.
Missing entries of heterogeneous dictionaries are filled up with `NaN` in the
resulting `DataFrame`:

```python
>>> pd.DataFrame([{'a': 1, 'b': 2}, {'a': 5, 'c': 4}])
   a    b    c
0  1  2.0  NaN
1  5  NaN  4.0
```

If a dictionary of `Series` is provided, each `Series` becomes a column with
its key mapped as the column name:

```python
>>> s1 = pd.Series([2, 4, 6, 8])
>>> s2 = pd.Series[(3, 6, 9, 12])
>>> pd.DataFrame({'two': s1, 'three': s2})
   two  three
0    2      3
1    4      6
2    6      9
3    8     12
```

If a two-dimensional NumPy array is provided, the numeric column and row
indices from the array are used, but can be set using the optional `columns`
and `index` parameters:

```python
>>> arr = np.arange(1, 10).reshape(3, 3)
>>> pd.DataFrame(arr)
   0  1  2
0  1  2  3
1  4  5  6
2  7  8  9

>>> pd.DataFrame(arr, columns=['A', 'B', 'C'], index=[1, 2, 3])
   A  B  C
1  1  2  3
2  4  5  6
3  7  8  9
```

If a structured NumPy array is provided, the field names serve as column names:

```python
>>> employees = np.zeros(3, dtype=np.dtype([('name', 'S10'), ('wage', 'f8')]))
>>> employees['name'] = ['Dilbert', 'Wally', 'Alice']
>>> employees['wage'] = [120000.00, 80000.00, 110000.00]
>>> pd.DataFrame(employees)
         name      wage
0  b'Dilbert'  120000.0
1    b'Wally'   80000.0
2    b'Alice'  110000.0
```

### Access: Indexing and Selection

The `DataFrame` for the following examples:

```python
>>> population = {
... 'USA': 326625792,
... 'Russia': 142257520,
... 'Germany': 80594016,
... 'Switzerland': 8236303
... }

>>> area = {
... 'USA': 9147593,
... 'Russia': 16377742,
... 'Germany': 348672,
... 'Switzerland': 39997
... }

>>> data = pd.DataFrame({'pop': population, 'area': area})
>>> data
                   pop      area
Germany       80594016    348672
Russia       142257520  16377742
Switzerland    8236303     39997
USA          326625792   9147593
```

Individual columns can be accessed either dictionary-style or attribute-style,
however the latter only works for columns with a string index that isn't used
for any other `DataFrame` attribute:

```python
>>> data['area']
Germany          348672
Russia         16377742
Switzerland       39997
USA             9147593
Name: area, dtype: int64

>>> data.area
Germany          348672
Russia         16377742
Switzerland       39997
USA             9147593
Name: area, dtype: int64

>>> data['area'] is data.area
True

>>> data['pop'] is data.pop
False # pop is a method of DataFrame!
```

For assignments, only dictionary-style access works (on the left side):

```python
>>> data['density'] = data['pop'] / data.area
>>> data
                   pop      area     density
Germany       80594016    348672  231.145650
Russia       142257520  16377742    8.686028
Switzerland    8236303     39997  205.923019
USA          326625792   9147593   35.706201
```

The raw, underlying multi-dimensional array of data of a `DataFrame` can be
accessed using the `value` attribute, which supports array-style indexing:

```python
>>> data.values
array([[8.05940160e+07, 3.48672000e+05, 2.31145650e+02],
       [1.42257520e+08, 1.63777420e+07, 8.68602766e+00],
       [8.23630300e+06, 3.99970000e+04, 2.05923019e+02],
       [3.26625792e+08, 9.14759300e+06, 3.57062007e+01]])

>>> data.values[0, 0]
80594016.0
```

A transposed version of the `DataFrame` (which rows and columns swapped) can be
accessed using the `T` attribute:

```python
>>> data.T
              Germany        Russia   Switzerland           USA
pop      8.059402e+07  1.422575e+08  8.236303e+06  3.266258e+08
area     3.486720e+05  1.637774e+07  3.999700e+04  9.147593e+06
density  2.311456e+02  8.686028e+00  2.059230e+02  3.570620e+01
```

A `DataFrame` offers different index attributes:

- `loc`: explicit index to access values by column and row _names_
    - inclusive upper bound
    - supports name based slicing, masking, fancy indexing
- `iloc`: implicit index to access values by column and row _numbers_
    - zero-based, exclusive upper bound
    - supports row and column access by ordinal numbers

```python
>>> data.loc['Germany':'Russia', 'pop':'area']
               pop      area
Germany   80594016    348672
Russia   142257520  16377742

>>> data.loc[data.density > 100, ['pop', 'density']]
                  pop     density
Germany      80594016  231.145650
Switzerland   8236303  205.923019

>>> data.iloc[0:2, 0:2]
               pop      area
Germany   80594016    348672
Russia   142257520  16377742
```

## Index

The Pandas `Index` is an immutable array/a ordered (multi)set that is used both
for the indexing of `Series` and `DataFrame`.

An `Index` can be created from a list:

```python
>>> pd.Index([1, 2, 3, 4, 5])
Int64Index([1, 2, 3, 4, 5], dtype='int64')
```

The elements of the `Index` can be accessed like list entries, i.e. by a single
index and using slicing:

```python
>>> idx = pd.Index([1, 2, 3, 4, 5])
>>> idx[2]
3

>>> idx[0:2]
Int64Index([1, 2], dtype='int64')

>>> idx[::2]
Int64Index([1, 3, 5], dtype='int64')
```

An `Index` is immutable, which is important when they are shared between
different `DataFrame`s and `Series`:

```python
>>> idx[2] = 6
TypeError: Index does not support mutable operations
```

Like Python's native set, `Index` supports set operations like intersection,
union and difference:

```python
>>> idxA.intersection(idxB)
Int64Index([1, 3, 5], dtype='int64')

>>> idxA.union(idxB)
Int64Index([1, 2, 3, 4, 5, 7, 9], dtype='int64')

>>> idxA.difference(idxB)
Int64Index([7, 9], dtype='int64')

>>> idxB.difference(idxA)
Int64Index([2, 4], dtype='int64')

>>> idxA.symmetric_difference(idxB)
Int64Index([2, 4, 7, 9], dtype='int64')
```

Union, intersection and symmetric difference can be expressed by the means of
operators:

```python
>>> idxA & idxB # intersection
Int64Index([1, 3, 5], dtype='int64')

>>> idxA | idxB # union
Int64Index([1, 2, 3, 4, 5, 7, 9], dtype='int64')

>>> idxA ^ idxB # symmetric difference
Int64Index([2, 4, 7, 9], dtype='int64')
```

## Operations

Pandas offers a lot of functions like NumPy's UFuncs that can be applied on a
`Series` or `DataFrame` either using a method (with another `Seris` or
`DataFrame` as a argument) or using a Python operator:

| Operator    | Method                           | Description         |
|-------------|----------------------------------|---------------------|
| `+`         | `add()`                          | Addition            |
| `-`         | `sub()`, `subtract()`            | Subtraction         |
| `*`         | `mul()`, `multiply()`            | Multiplication      |
| `/`         | `truediv()`, `div()`, `divide()` | Division            |
| `//`        | `floordiv()`                     | Floor Division      |
| `%`         | `mod()`                          | Modulus (remainder) |
| `**`        | `pow()`                          | Exponentiation      |

The index of the operands is preserved in the result. If the operands are
heterogeneous, the result contains the union of the two indices, with `NaN`
filled in for missing values:

```python
>>> hours = pd.Series([25, 40, 32], index=['Alice', 'Bob', 'Malory'])
>>> rates = pd.Series([45, 50, 30], index=['Alice', 'Bob', 'Thomas'])
>>> hours * wages
Alice     1125.0
Bob       2000.0
Malory       NaN
Thomas       NaN
dtype: float64
```

An operation that mixes a `Series` and a `DataFrame` works like an operation on
a one-dimensional and a multi-dimensional array; broadcasting rules (similar as
those for NumPy) apply:

```python
>>> wages = pd.DataFrame({'January': {'Alice': 4500, 'Bob': 4800},
...                       'February': {'Alice': 4200, 'Bob': 4500}})
>>> wages
       January  February
Alice     4500      4200
Bob       4800      4500

>>> increase = pd.Series({'Alice': 1.2, 'Bob': 1.1})
>>> increase
Alice    1.2
Bob      1.1
dtype: float64

>>> wages.T * increase # with transposition
           Alice     Bob
January   5400.0  5280.0
February  5040.0  4950.0

>>> wages.multiply(increase, axis=0) # with optional axis (increase as rows)
       January  February
Alice   5400.0    5040.0
Bob     5280.0    4950.0
```

Pandas always preserves indices and column names, so that the data context is
maintained.

## Handling Missing Data

Real-world data sets are rarely clean and homogeneous. Oftentimes, values are
missing, and the lack of a value is indicated in different ways. Pandas marks
the absence of a value in two different ways:

1. `None`: a Python singleton object, which is used in `object` collections
   (rather slow due to the overhead).
2. `NaN`: a special floating point value (not a number), which is defined in
   the IEEE-754 standard and used for numeric collections. NumPy's `NaN`
   reference is used: `np.nan`.

A `Series` and `DataFrame` containing a `None` or `NaN` «value» is upcast
according to the types of the other elements: integer types are upcast to
`float64`; booleans are upcast to `object`.

```python
>>> pd.Series([1, 2, None]) # None replaced by NaN
0    1.0
1    2.0
2    NaN
dtype: float64

>>> pd.Series([1, 2, np.nan])
0    1.0
1    2.0
2    NaN
dtype: float64

>>> pd.Series([True, False, None]) # None preserved
0     True
1    False
2     None
dtype: object

>>> pd.Series([True, False, np.nan])
0     True
1    False
2      NaN
dtype: object
```

Any operation involving `NaN` yields `NaN`:

```python
>>> 3 + np.nan
nan

>>> (3 + 7) * np.nan
nan

>>> pd.Series([1, 2, np.nan]) + pd.Series([1, np.nan, 3])
0    2.0
1    NaN
2    NaN
dtype: float64
```

Whereas NumPy supports special `NaN`-aware functions (`np.nansum()`,
`np.nanmax()`), Pandas offers special functions to deal with absent values:

`isnull()` and `notnull()` return a boolean mask indicating if there is no
value (`isnull`) or a value (`notnull`) at the respective index. These masks
can be used for indexing:

```python
>>> s = pd.Series([1, np.nan, 3])
>>> s.isnull()
0    False
1     True
2    False
dtype: bool

>>> s.notnull()
0     True
1    False
2     True
dtype: bool

>>> s[s.notnull()]
0    1.0
2    3.0
dtype: float64
```

`dropna()` removes `None` and `NaN` entries in a `Series`. In a `DataFrame`,
the full row or column missing a value is removed, which can be defined using
the optional `axis` parameter:

```python
>>> farmers = ['Miller', 'Shaw', 'Watson']
>>> dogs = pd.Series([1, 2, 1], index=farmers)
>>> cats = pd.Series([3, 1, np.nan], index=farmers)
>>> cows = pd.Series([7, np.nan, 2], index=farmers)
>>> pigs = pd.Series([0, 2, np.nan], index=farmers)
>>> livestock = pd.DataFrame( {'dogs': dogs, 'cats': cats, 'cows': cows, 'pigs': pigs})
>>> livestock
        dogs  cats  cows  pigs
Miller     1   3.0   7.0   0.0
Shaw       2   1.0   NaN   2.0
Watson     1   NaN   2.0   NaN

>>> livestock.dropna() # default: axis='rows'
        dogs  cats  cows  pigs
Miller     1   3.0   7.0   0.0

>>> livestock.dropna(axis='columns')
        dogs
Miller     1
Shaw       2
Watson     1
```

By default, every row/column with at least one missing entry is dropped. If the
optional `how` parameter is set to `all`, only rows/columns with missing values
only are dropped:

```pythpon
>>> livestock.dropna() # default: how='any'
        dogs  cats  cows  pigs
Miller     1   3.0   7.0   0.0

>>> livestock.dropna(how='all')
        dogs  cats  cows  pigs
Miller     1   3.0   7.0   0.0
Shaw       2   1.0   NaN   2.0
Watson     1   NaN   2.0   NaN
```

The optional parameter `thresh` allows to define a threshold: only drop
rows/columns with fewer values given:

```python
>>> livestock.dropna(thresh=3) # drop rows with fewer than three values
        dogs  cats  cows  pigs
Miller     1   3.0   7.0   0.0
Shaw       2   1.0   NaN   2.0

>>> livestock.dropna(thresh=3, axis='columns')
        dogs
Miller     1
Shaw       2
Watson     1
```

`fillna()` fills in a value where one is missing. Either a scalar value can be
passed, or the value from a neighbouring cell can be propagated using a
combination of the `method` (`ffill`/`bfill`: forward and backward fill) and
`axis` (`rows`/`columns`) parameters:

```python
>>> livestock.fillna(0) # replace NaN with 0, which is useful for sums
        dogs  cats  cows  pigs
Miller     1   3.0   7.0   0.0
Shaw       2   1.0   0.0   2.0
Watson     1   0.0   2.0   0.0

>>> livestock.fillna(method='ffill', axis='rows') # propagate value to next row
        dogs  cats  cows  pigs
Miller     1   3.0   7.0   0.0
Shaw       2   1.0   7.0   2.0
Watson     1   1.0   2.0   2.0

>>> livestock.fillna(method='bfill', axis='columns') # ... from previous column
        dogs  cats  cows  pigs
Miller   1.0   3.0   7.0   0.0
Shaw     2.0   1.0   2.0   2.0
Watson   1.0   2.0   2.0   NaN
```

If there is no next or previous row or column, `NaN` entries could still remain
after the `fillna()` operation.
