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

## Hierarchical Indexing

Pandas `Series` and `DataFrame` represent one- and two-dimensional data. But
some data must be indexed by more than two indices, and values can only be
accessed by a combination of all those indices. This concept is called
_hierarchical indexing_ or _multi-indexing_.

A index with multiple levels could be represented by a tuple (using Formula 1
teams and seasons as indices):

```python
>>> index = [
    ('Mercedes', 2018), ('Mercedes', 2017),
    ('Ferrari', 2018), ('Ferrari', 2017),
    ('McLaren', 2018), ('McLaren', 2017)]
>>> points = pd.Series([655, 688, 571, 522, 62, 30], index=index)
>>> points
(Mercedes, 2018)    655
(Mercedes, 2017)    688
(Ferrari, 2018)     571
(Ferrari, 2017)     522
(McLaren, 2018)      62
(McLaren, 2017)      30
dtype: int64
```

However, storing a tuple as the index is inconvenient and inefficient for data
access. Therefore Pandas offers `MultiIndex`, an efficient wrapper for tuple
indices:

```python
>>> multi_index = pd.MultiIndex.from_tuples(index)
>>> multi_index
MultiIndex(levels=[['Ferrari', 'McLaren', 'Mercedes'], [2017, 2018]],
           labels=[[2, 2, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0]])
```

The `MultiIndex` has two `levels` (the team names and seasons), and they are
combined with `labels` like this:

| Team     | `labels[0]` | `labels[1]` | Season |
|----------|-------------|-------------|--------|
| Mercedes | 2           | 1           | 2018   |
| Mercedes | 2           | 0           | 2017   |
| Ferrari  | 0           | 1           | 2018   |
| Ferrari  | 0           | 0           | 2017   |
| McLaren  | 1           | 1           | 2018   |
| McLaren  | 1           | 0           | 2017   |

A `Series` created with a tuple index can be reindexed using a `MultiIndex`:

```python
>>> points = points.reindex(multi_index)
>>> points
Mercedes  2018    655
          2017    688
Ferrari   2018    571
          2017    522
McLaren   2018     62
          2017     30
dtype: int64
```

The blank space below the team index means that the value from above is used.

Conceputally, a `Series` with two indices is a lot like a `DataFrame`, which
maps the first index to the rows and the second index to the columns. A
multi-index `Series` can be converted to a `DataFrame` using the `Series`
`unstack()` method:

```python
>>> points_df = points.unstack()
>>> points
          2017  2018
Ferrari    522   571
McLaren     30    62
Mercedes   688   655
```

The `DataFrame` can be converted back to a multi-index `Series` using the
`stack()` method:

```python
>>> points_sr = points_df.stack()
Ferrari   2017    522
          2018    571
McLaren   2017     30
          2018     62
Mercedes  2017    688
          2018    655
dtype: int64
```

A `DataFrame` with additional columns can be created based on the existing
`DataFrame`:

```python
>>> f1 = pd.DataFrame({
    'points': points,
    'races': [21, 20, 21, 20, 21, 20],
    'wins': [11, 12, 6, 5, 0, 0]})
>>> f1
               points  races  wins
Mercedes 2018     655     21    11
         2017     688     20    12
Ferrari  2018     571     21     6
         2017     522     20     5
McLaren  2018      62     21     0
         2017      30     20     0
```

The operations mentioned earlier can also be applied:

```python
>>> win_ratio = f1['wins'] / f1['races']
>>> win_ratio
Mercedes  2018    0.523810
          2017    0.600000
Ferrari   2018    0.285714
          2017    0.250000
McLaren   2018    0.000000
          2017    0.000000
dtype: float64
```

### Creation of Hierarchical Indices

A hierarchical index can be created implicitly, i.e. together with the `Series`
or the `DataFrame`.

The index can be passed as an additional argument to the constructor as a list
of index arrays:

```python
>>> points = [655, 688, 571, 522]
>>> index = [['Mercedes', 'Mercedes', 'Ferrari', 'Ferrari'],
             [2018, 2017, 2018, 2017]]
>>> pd.Series(points, index=index)
Mercedes  2018    655
          2017    688
Ferrari   2018    571
          2017    522
dtype: int64
```

Or a dictionary can be passed to the constructor, with appropriate index tuples
as keys:

```python
>>> points = {('Mercedes', 2018): 655, ('Mercedes', 2017): 688,
              ('Ferrari', 2018): 571, ('Ferrari', 2017): 522}
>>> pd.Series(points)
Mercedes  2018    655
          2017    688
Ferrari   2018    571
          2017    522
dtype: int64
```

Using one of `MultiIndex` class methods, a hierarchical index can be created
explicitly. The resulting object can be passed to the constructor of a `Series`
or a `DataFrame` as the `index` attribute.

The method `from_arrays` accepts a list of index arrays:

```python
>>> pd.MultiIndex.from_arrays([['Mercedes', 'Mercedes', 'Ferrari', 'Ferrari'],
                               [2018, 2017, 2018, 2017]])
MultiIndex(levels=[['Ferrari', 'Mercedes'], [2017, 2018]],
           labels=[[1, 1, 0, 0], [1, 0, 1, 0]])
```

The method `from_tuples` accepts a list of index tuples:

```python
>>> pd.MultiIndex.from_tuples([('Mercedes', 2018), ('Mercedes', 2017),
                               ('Ferrari', 2018), ('Ferrari', 2017)])
MultiIndex(levels=[['Ferrari', 'Mercedes'], [2017, 2018]],
           labels=[[1, 1, 0, 0], [1, 0, 1, 0]])
```

In the above examples, every item from the first index (`['Mercedes',
'Ferrari']`) has been combined with every item from the second index (`[2018,
2017]`) _manually_. This Cartesian product can also be created automatically
using the `from_product` method:

```python
>>> pd.MultiIndex.from_product([['Mercedes', 'Ferrari'], [2018, 2017]])
MultiIndex(levels=[['Ferrari', 'Mercedes'], [2017, 2018]],
           labels=[[1, 1, 0, 0], [1, 0, 1, 0]])
```

The index levels can also be combined manually using a nested list of labels
passed to the constructor of `MultiIndex`. This is especially helpful, if only
certain combinations of index entries need to be created:

```python
>>> index = pd.MultiIndex(levels=[['Manor', 'Haas'], [2015, 2016, 2017]],
                          labels=[[0,0,1,1], [0,1,1,2]])
>>> pd.Series([0, 1, 29, 47], index=index)
Manor  2015     0
       2016     1
Haas   2016    29
       2017    47
dtype: int64
```

Using a `DataFrame`, both rows and columns can have multiple indices:

```python
>>> row_index = pd.MultiIndex.from_product([['Mercedes', 'Ferrari'],
                                            [2018, 2017]])
>>> col_index = pd.MultiIndex.from_product([['Australia', 'Bahrain'],
                                            ['Driver 1', 'Driver 2']])
>>> pos = np.array([2, 8, 3, 2, 2, 3, 2, 3, 1, 3, 1, np.nan, 1, 4, 1, 4])
>>> f1 = pd.DataFrame(pos.reshape((4, 4)), index=row_index, columns=col_index)
>>> f1
              Australia           Bahrain
               Driver 1 Driver 2 Driver 1 Driver 2
Mercedes 2018       2.0      8.0      3.0      2.0
         2017       2.0      3.0      2.0      3.0
Ferrari  2018       1.0      3.0      1.0      NaN
         2017       1.0      4.0      1.0      4.0
```

This allows for four-dimensional indices.

Both row and column index can be named by setting a list of row/column names
with the appropriate length to the `names` attribute of the index:

```python
>>> f1.index.names = ['Team', 'Season']
>>> f1.columns.names = ['GP', 'Driver']
>>> f1
GP              Australia           Bahrain
Driver           Driver 1 Driver 2 Driver 1 Driver 2
Team     Season
Mercedes 2018         2.0      8.0      3.0      2.0
         2017         2.0      3.0      2.0      3.0
Ferrari  2018         1.0      3.0      1.0      NaN
         2017         1.0      4.0      1.0      4.0
```

### Indexing and Slicing

Indexing and Slicing on `Series` is row based. This `Series` index has a
species as the first (higher level) index, and the year as the second (lower
level) index:

```python
>>> idx = pd.MultiIndex.from_product([['cats', 'cows', 'dogs', 'pigs'],
                                        [2000, 2005, 2010]])
>>> livestock = pd.Series([32, 16, 25, 60, 75, 52, 1, 1, 2, 4, 3, 7], index=idx)
>>> livestock
cows  2000    32
      2005    16
      2010    25
pigs  2000    60
      2005    75
      2010    52
dogs  2000     1
      2005     1
      2010     2
cats  2000     4
      2005     3
      2010     7
dtype: int64
```

Individual values can be accessed using full indexing by first indicating the
higher level index and second the lower level index:

```python
>>> livestock['cats', 2000]
4
>>> livestock['cows', 2010]
25
>>> livestock['pigs', 2005] - livestock['pigs', 2010]
23
```

If the lower level index is left unspecified, a `Series` with the lower level
index retained is returned:

```python
>>> livestock['cows']
2000    32
2005    16
2010    25
dtype: int64
```

Passing an empty slice for the higher level index allows indexing on the lower
level index:

```python
>>> livestock[:, 2010]
cows    25
pigs    52
dogs     2
cats     7
dtype: int64
```

Slicing on the explicit index is only available on a sorted `MultiIndex`:

```python
>>> idx = idx.sort_values()
>>> livestock = pd.Series([4, 3, 7, 32, 16, 25, 1, 1, 2, 60, 75, 52], index=idx)
>>> livestock.loc['cats':'cows', 2000:2005]
cats  2000     4
      2005     3
cows  2000    32
      2005    16
dtype: int64
```

Selections can be made based on boolean masks:

```python
>>> livestock[livestock > 10]
cows  2000    32
      2005    16
      2010    25
pigs  2000    60
      2005    75
      2010    52
dtype: int64
```

Values can be selected using fancy indexing:

```python
>>> livestock[['cows', 'pigs']]
cows  2000    32
      2005    16
      2010    25
pigs  2000    60
      2005    75
      2010    52
dtype: int64
```

The indexing hierarchy on a `DataFrame` behaves like the one of a `Series`,
expect that a `DataFrame` is indexed by columns first:

```python
>>> row_idx = pd.MultiIndex.from_product([[2017, 2018],
                                          ['Jan', 'Jul']])
>>> col_idx = col_idx = pd.MultiIndex.from_product([['Tom', 'Jim'],
                                                    ['height', 'weight']])
>>> val = [[122, 35, 129, 37],
           [128, 37, 131, 39],
           [134, 39, 135, 41],
           [137, 40, 138, 43]]
>>> kids = pd.DataFrame(val, columns=col_idx, index=row_idx)
>>> kids
            Tom           Jim
         height weight height weight
2017 Jan    122     35    129     37
     Jul    128     37    131     39
2018 Jan    134     39    135     41
     Jul    137     40    138     43

>>> kids['Tom', 'height']
2017  Jan    122
      Jul    128
2018  Jan    134
      Jul    137
Name: (Tom, height), dtype: int64
```

For row-oriented selection on a `DataFrame`, the implicit index can be used:

```python
>>> kids.iloc[0:2]
            Tom           Jim
         height weight height weight
2017 Jan    122     35    129     37
     Jul    128     37    131     39
```

The column index hierarchy can be expressed using the explicit index and
tuples:

```python
>>> kids.loc[:, ('Tom', 'weight')]
2017  Jan    35
      Jul    37
2018  Jan    39
      Jul    40
Name: (Tom, weight), dtype: int64
```

Because tuples do not support slices, Pandas offers the `IndexSlice` object:

```python
>>> jan = pd.IndexSlice[:, 'Jan']
>>> weight = pd.IndexSlice[:, 'weight']
>>> kids.loc[jan, weight]
            Tom    Jim
         weight weight
2017 Jan     35     37
2018 Jan     39     41
```
