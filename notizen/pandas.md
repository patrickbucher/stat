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
