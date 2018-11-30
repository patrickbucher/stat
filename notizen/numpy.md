# NumPy

Arrays of numbers are the fundamental data structure for data analysis.
Python's primitive values have a large overhead. This information is redundant
in lists, because the same type information is stored for every element. NumPy
arrays are much more efficent than Python's lists―especially for big data sets.
Python also offers an array type without redundant type information. However,
this array type doesn't offer the fast and powerful operations of NumPy's
`ndarray` type.

Conventionally, the NumPy library is imported as follows:

```python
import numpy as np
```

## Array Creation

### Arrays of Python Lists

NumPy arrays can be created from Python lists:

```python
ints = np.array([2, 4, 6, 8]) # integer array
floats = np.array([2, 4, 6, 8.1]) # upcast to float because of 8.1
floats = np.array([2, 4, 6, 8], dtype='float') # with explicit type parameter
ints = np.array([1.1, 2.2, 3.3], dtype='int') # with explicit type parameter
```

NumPy arrays can be multi-dimensional:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
```

### Arrays from Scratch

Numpy offers various functions to generate arrays from scratch. Where a
dimension is required (`size`), a single number (length), a tuple of two (rows,
columns) or more (1st dimension, 2nd dimension, 3rd dimension, etc.) can be
passed.

- `np.zeros(size, dtype)`: array of zeros
- `np.ones(size, dtype)`: array of ones
- `np.full(size, value)`: array filled with the given value
- `np.arange(start, end, step)`: array with values from start (inclusive) to
  end (exclusive) and given step width; `length=(end-start)/step`
- `np.linspace(from, to, n)`: array with evenly spaced values in interval
  `[from,to]` (both inclusive) of length n
- `np.random.random(size)`: uniformly distributed random values
- `np.random.normal(mean, sd, size)`: normally distributed array with the given
  mean and standard deviation
- `np.random.randint(from, to, size)`: random integers in the interval
  `[from,to)` (inclusive/exclusive)
- `np.eye(n)`: identity matrix with n rows and columns (values at indices with
  equal row/column index are 1)
- `np.empty(size)`: uninitialized array, values from current memory content
  (garbage)

### Data Types

The `dtype` parameter can either be passed as a string literal or using a
pre-defined constant:

1. literal: `dtype='int32'`
2. constant: `dtype=np.int32`

Common numeric types are:

- boolean: `Bool_`
- signed integers: `int8`, `int16`, `int32`, `int64`
    - `int_`: system's default `long`
    - `intc`: system's default `int`
- unsigned integers: `uint8`, `uint16`, `uint32`, `uint64`
- floating point: `float16`, `float32`, `float64` 
    - `float_`: system default
- complex numbers: `complex64`, `complex128`
    - `complex_`: system default

## Array Manipulation

NumPy arrays offer a rich set of attributes and operation for their manipulation. Since NumPy arrays are the foundation of many higher-level libraries, data manipulation in Python is often NumPy array manipulation.

### Attributes

These read-only attributes can be used to retrieve information about an array:

- `ndim`: number of dimensions
- `shape`: size of each dimension
- `size`: total size of the array (the number of elements)
- `dtype`: data type of the array's elements
- `itemsize`: byte size of a single element
- `nbytes`: byte size of the entire array

In general, `nbytes` is equal to `itemsize` multiplied by `size`.

```python
>>> np.random.seed(0) # for reproducable results
>>> arr = np.random.randint(10, 100, (3, 3))
>>> arr
array([[54, 57, 74],
       [77, 77, 19],
       [93, 31, 46])
>>> arr.ndim
2
>>> arr.shape
(3, 3)
>>> arr.size
9
>>> arr.dtype
dtype('int64')
>>> arr.itemsize
8
>>> arr.nbytes
72
>>> arr.itemsize * arr.size
72
```

### Indexing

Values of NumPy arrays can both be retrieved and modified by the means of
indexing.

The indexing of single dimension arrays works with square brackets, just like
indexing of Python lists:

- `arr[0]`: first element
- `arr[n]`: nth element
- `arr[-1]`: last element (first element counted from the end)
- `arr[-3]`: third last element (third element counted from the end)

For multi dimension arrays, a comma separated tuple has to be passed in square
brackets:

- `arr[0, 0]`: first element of the first dimension
- `arr[3, 5]`: fifth element of the third dimension

```python
>>> np.random.seed(0) # for reproducable results
>>> arr = np.random.randint(10, 100, (3, 3))
>>> arr
array([[54, 57, 74],
       [77, 77, 19],
       [93, 31, 46])

>>> arr[0, 0]
54

>>> arr[1, 2]
19

>>> arr[-1, -1]
46

>>> arr[2, 2]
46
```

### Slicing

The slicing syntax of Python lists also works for NumPy arrays:

- `[start:stop:step]`, with values omitted defaulting to:
    - `start=0`
    - `stop=[size of dimension]`
    - `step=1`
- For a negative step size, the defaults for `start` and `stop` are swapped.

```python
>>> arr = np.arange(1, 10)
>>> arr
array([1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> arr[2:5] # third (inclusive) to fifth (exclusive)
array([3, 4, 5])

>>> arr[::2] # every other (beginning with first)
array([1, 3, 5, 7])

>>> arr[::-1] # reversed
array([9, 8, 7, 6, 5, 4, 3, 2, 1])
```

If a step is indicated, two colons are required. Otherwise, step is interpreted
as the stop.

Multi-dimension arrays can be sliced by providing multiple, comma-separated
slices:

- `[start1:stop1:step1, start2:stop2:step2]`, for slicing the first and second
  dimension.
- Indexing and slicing can be combined in order to access individual
  columns/rows:
    - `[:, 0]`: all rows, first column
    - `[0, :]`: first row, all columns
        - `[0]`: shorthand (`:` can be omitted)

```python
>>> np.random.seed(0) # for reproducable results
>>> arr = np.random.randint(10, 100, (3, 3))
>>> arr
array([[54, 57, 74],
       [77, 77, 19],
       [93, 31, 46])

>>> arr[::2, 0:2] # columns 0 and 1 of every other row
array([[54, 57],
       [93, 31]])

>>> arr[:, 0] # first column
array([54, 77, 93])

>>> arr[0, :] # first row
array([54, 57, 74])

>>> arr[0] # first row (shorthand)
array([54, 57, 74])
```

Unlike Python lists, slices of NumPy arrays are _views to_ the original data,
not _copies of_ it. To get a copy of a slice that can be modified without
affecting the underlying array, the `copy()` method can be used. Using the
array from above:

```python
>>> s = arr[::2, 0:2] # view on columns 0 and 1 of every other row
>>> s
array([[54, 57],
       [93, 31]])

>>> s[0,1] = 88
>>> s[1,0] = 99
>>> s
array([[54, 88],
       [99, 31]])

>>> t = arr[1, 0:2].copy() # copy of columns 0 and 1 of the second row
>>> t
array([77, 77])

>>> t[0] = 11
>>> t[1] = 22
>>> t
array([11, 22])

>>> arr
array([[54, 88, 74],  # 88 introduced through s
       [77, 77, 19],  # 11 and 22 missing (working on copy t)
       [99, 31, 46]]) # 99 introduced through s
```

### Reshaping

There are two options to reshape an existing array:

1. The function `reshape(size)`, which reshapes the underlying array to the
   given size (dimension indications).
    - The new size must match the array's size.
    - Good: `arr.size=60`, `arr.reshape((6, 10))`, because `6*10=60`
    - Bad: `arr.size=16`, `arr.reshape((4, 6))`, because `4*6>16`
2. Using the slicing parameter `np.newaxis`, which converts a one-dimensional
   to a two-dimensional array.
    - `arr[np.newaxis, :]`: array elements as columns
    - `arr[:, np.newaxis]`: array elements as rows

Example:

```python
>>> np.arange(1, 10).reshape((3, 3))
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

>>> np.arange(1, 4)[np.newaxis, :]
array([[1, 2, 3]])

>>> np.arange(1, 4)[:, np.newaxis]
array([[1],
       [2],
       [3]])
```

### Concatenation

The options to concatenate arrays of same and different dimensions are:

1. The function `np.concatenate(arrays, axis)`, which works on arrays of the
   same dimensions.
    - `arrays`: a list or tuple of arrays
    - `axis`: index of the axis, along which the concatenation takes place (0:
      rows, 1: columns, 2: third dimension)
2. Functions, which concatenate the given arrays of (possible) different
   dimensions:
    - `np.vstack(arrays)`: stack the arrays vertically
    - `np.hstack(arrays)`: stack the arrays horizontally
    - `np.dstack(arrays)`: stack the arrays along the third dimension

Example:

```python
>>> a = np.arange(1, 5) # 1, 2, 3, 4
>>> b = np.arange(5, 9) # 5, 6, 7, 8
>>> np.concatenate((a, b))
array([1, 2, 3, 4, 5, 6, 7, 8])

>>> x = a.reshape((2, 2))
>>> x
array([[1, 2],
       [3, 4]])

>>> y = b.reshape((2, 2))
>>> y
array([[5, 6],
       [7, 8]])

>>> np.concatenate((x, y), axis=0) # along rows
array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])

>>> np.vstack((x, y)) # same, but shorter
array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])

>>> np.concatenate((x, y), axis=1) # along columns
array([[1, 2, 5, 6],
       [3, 4, 7, 8]])

>>> np.hstack((x, y)) # same, but shorter
array([[1, 2, 5, 6],
       [3, 4, 7, 8]])

>>> i = np.arange(1, 4).reshape((3, 1))
>>> i
array([[1],
       [2],
       [3]])

>>> j = np.arange(4, 10).reshape(3, 2)
>>> j
array([[4, 5],
       [6, 7],
       [8, 9]])

>>> np.hstack((i, j))
array([[1, 4, 5],
       [2, 6, 7],
       [3, 8, 9]])

>>> m = np.arange(1, 4)
>>> m
array([1, 2, 3])

>>> n = np.arange(4, 10).reshape((2, 3))
>>> n
array([[4, 5, 6],
       [7, 8, 9]])

>>> np.vstack((m, n))
array([[1, 2, 4],
       [4, 5, 6],
       [7, 8, 9]])
```

### Splitting

An array split up at `N` split points will result in `N+1` arrays. As for
reshaping and concatenation, there are two fundamental ways to split arrays:

1. The function `np.split(array, splitpoints)`.
    - `array`: an array of any dimension
    - `splitpoints`: a list of indices
        - a divider (positive integer value) can be used to split the array up
          into `n` equally sized chunks
2. Functions, which split an array along a specific dimension.
    - `np.hsplit(array, splitpoints)`: split the array along the horizontal
      axis
    - `np.vsplit(array, splitpoints)`: split the array along the vertically
      axis
    - `np.dsplit(array, splitpoints)`: split the array along a third dimension

Example:

```python
>>> a = np.arange(1, 9)
>>> a
array([1, 2, 3, 4, 5, 6, 7, 8])

>>> np.split(a, [4]) # split at index 4 (beginning of second chunk)
[array([1, 2, 3, 4]), array([5, 6, 7, 8])]

>>> np.split(a, 2) # divide into 2 equally sized parts
[array([1, 2, 3, 4]), array([5, 6, 7, 8])]

>>> np.split(a, [2, 6]) # split at indices 2 and 6
[array([1, 2]), array([3, 4, 5, 6]), array([7, 8])]

>>> b = np.arange(1, 10).reshape((3, 3))
>>> b
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

>>> i, j = np.hsplit(b, [2]) # split off first two columns
>>> i
array([[1, 2],
       [4, 5],
       [7, 8]])

>>> j
array([[3],
       [6],
       [9]])

>>> m, n = np.vsplit(b, [1]) # split off first row
>>> m
array([[1, 2, 3]])

>>> n
array([[4, 5, 6],
       [7, 8, 9]])
```

## Universal Functions

- Loop-based operations on arrays resp. on their elements are slow, because
  Python performs type-checks and lookups for every function calll.
- NumPy's universal functions (UFuncs) are statically typed and compiled. They
  can be performed on an array as a whole―and will be applied to each element.
  This is much faster and more convenient.
    - Loops over arrays should be rewritten in terms of UFuncs. The bigger the
      array, the larger the gain.
- UFuncs can be applied:
    - to an array and a scalar value:
        - `np.arange(1, 4) * 2 # [2, 4, 6]`
    - to an array and another array:
        - `np.arange(1, 4) * np.arange(7, 10) # [8, 10, 12]`

### Common UFuncs

Many of Python's native operators can be used as shorthands for UFuncs:

| Shorthand   | UFunc             | Description         |
|-------------|-------------------|---------------------|
| `+`         | `np.add`          | Addition            |
| `-`         | `np.subtract`     | Subtraction         |
| `-` (unary) | `np.negative`     | Negative Prefix     |
| `*`         | `np.multiply`     | Multiplication      |
| `/`         | `np.divide`       | Division            |
| `//`        | `np.floor_divide` | Floor Division      |
| `**`        | `np.power`        | Exponentiation      |
| `%`         | `np.mod`          | Modulus (remainder) |
| `np.abs`    | `np.absolute`     | Absolute value      |

There are a lot of additional mathematical UFuncs:

- `np.sin`/`np.arcsin`: Sine and Arcsine
- `np.cos`/`np.arccos`: Cosine and Arcosine
- `np.tan`/`np.arctan`: Tangents and Cotangents
- `np.exp2`: `2^x`
- `np.exp`: `e^x`
- `np.log`: base-e logarithm
- `np.log2`: base-2 logarithm
- `np.log10`: base-10 logarithm

### Advanced Features

Rather than creating a new array for the return value, the result of a UFunc
can be stored in an existing array using the `out` parameter. This also works
with slices:

```python
>>> x = np.arange(1, 6)
>>> x
array([1, 2, 3, 4, 5])

>>> y = np.zeros(5, dtype=np.int)
>>> y
array([0, 0, 0, 0, 0])

>>> np.power(x, 2, out=y)
>>> y
array([1, 4, 9, 16, 25])

>>> z = np.zeros(10)
>>> z
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

>>> np.power(x, 2, out=z[::2]) # overwrite every other element
>>> z
array([1, 0, 4, 0, 9, 0, 16, 0, 25, 0])
```

Every UFunc comes with a `reduce` operation, which repeatedly applies an
operation to the elements of an array until only a single result remains.

```python
>>> x = np.arange(1, 5)
>>> x
array([1, 2, 3, 4, 5])

>>> np.add.reduce(x) # Sum: 1 + 2 + 3 + 4 + 5
15

>>> np.multiply.reduce(x) # Factorial: 1 * 2 * 3 * 4 * 5
120
```

Instead of just storing the end results, each intermediary step can be stored
using the `accumulate` function:

```python
>>> x = np.arange(1, 5)
>>> x
array([1, 2, 3, 4, 5])

>>> np.add.accumulate(x)
array([1, 3, 6, 10, 15)

>>> np.multiply.accumulate(x)
array([1, 2, 6, 24, 120])
```

The `outer` operation computes the output of all pairs of two inputs, which
could be used to create a multiplication table, for example:

```python
>>> a = np.arange(1, 6)
>>> a
array([1, 2, 3, 4, 5])

>>> b = np.arange(1, 9)[1::2]
>>> b
array([2, 4, 6, 8])

>>> np.multiply.outer(b, a) # column, row
array([[ 2,  4,  6,  8, 10],
       [ 4,  8, 12, 16, 20],
       [ 6, 12, 18, 24, 30],
       [ 8, 16, 24, 32, 40]])
```

| `*` | 1 | 2  | 3  | 4  | 5  |
|-----|---|----|----|----|----|
| 2   | 2 | 4  | 6  | 8  | 10 |
| 4   | 4 | 8  | 12 | 16 | 20 |
| 6   | 6 | 12 | 18 | 24 | 30 |
| 8   | 8 | 16 | 24 | 32 | 40 |

## Aggregations

Aggregations reduce an array or one of its dimensions to a single value. In
contrast to Python's built-in aggregate functions (`sum`, `min`, `max`),
NumPy's implementations can operate on multi-dimensional arrays―and are much
faster.

- Aggregate functions take an optional `axis` parameter, which describes _the
  array dimension to be collapsed_:
    - `axis=0`: collapse columns
    - `axis=1`: collapse rows

```python
>>> a = np.random.randint(1, 10, size=(3, 4))
>>> a
array([[7, 8, 5, 5],
       [6, 1, 7, 2],
       [7, 2, 8, 8]])

>>> a.sum()
66

>>> a.sum(axis=0)
array([20, 11, 20, 16])

>>> a.sum(axis=1)
array([25, 16, 25])
```

All aggregate functions can be called using the syntax `np.function(array,
[parameters])`. Except for `np.median` and `np.percentile`, the following
functions can be called directly on the array using the syntax
`array.function([parameters])`.

| Function             | Returns                         |
|----------------------|---------------------------------|
| `np.sum`             | sum                             |
| `np.prod`            | product                         |
| `np.min`             | minimum value                   |
| `np.max`             | maximum value                   |
| `np.argmin`          | index of minimum value          |
| `np.argmax`          | index of maximum value          |
| `np.mean`            | mean («average») value          |
| `np.median`          | median («middle») value         |
| `np.var`             | variance                        |
| `np.std`             | standard deviation              |
| `np.percentile(q=n)` | nth percentile, n in `[0, 100]` |
| `np.any`             | is _any_ value true?            |
| `np.all`             | are _all_ values true?          |

Special NaN-aware functions exist for every function (execpt for the boolean
functions `np.any` and `np.all`). They have the prefix `nan` and can only be
called on `nd`, not directly on the array. Since NaN belongs to the IEEE-754
standard, arrays containing NaN must have the type float or double.

```python
>>> a = np.array([1, 2, 3, np.NAN, 5])
>>> a
array([ 1.,  2.,  3., nan,  5.])

>>> np.sum(a)
nan

>>> np.nansum(a)
11.0
```
