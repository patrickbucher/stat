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
- `np.random.choice(a, size, replace, p)`: random values from the array `a` or
  up to the upper bound value `a` with (`replace=True`) or without
  (`replace=False`) replacement and an optional array of probabilities `p`
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

## Broadcasting

Broadcasting is a set of rules for applying binary UFuncs (addition,
multiplication, etc.) on arrays of different sizes and/or dimensions.

**Rule 1**: If the arrays have a different number of dimensions, the _shape_ of
the array with fewer dimensions is padded with ones on the left.

```python
>>> a = np.ones(9).reshape(3, 3)
>>> a
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])

>>> b = np.arange(1, 4)
>>> b
array([1, 2, 3])

>>> a.shape
(3, 3)

>>> b.shape
(3,)
```

**Result**: The shape of `b` is one-padded on the left: `(3,)` → `(1, 3)`.
Thus, `array([1, 2, 3])` becomes `array([[1, 2, 3]])`.

**Rule 2**: If the shape of the arrays does not match in any dimension, the
array with a shape of one is stretched in that dimension to match the other
shape.

**Result**: The rows of `b` are stretched (i.e. repeated), the shape changes
again: `(1, 3)` → `(3, 3)`. Thus, `array([[1, 2, 3]])` becomes:

```python
array([[1, 2, 3].
       [1, 2, 3],
       [1, 2, 3]])
```

This is only a _conceptual_ transformation, no memory is wasted when stretching!

3. If the dimensions neither match nor are equal to one, an error is raised.

```python
>>> x = np.ones(6).reshape(2, 3)
>>> x
array([[1., 1., 1.],
       [1., 1., 1.]])

>>> y = np.arange(1, 3)
>>> y
array([1, 2])

>>> x.shape
(2, 3)

>>> y.shape
(2,)
```

**Result**: Error.

In order to perform binary operations on incompatible arrays (according these
broadcasting rules), the arrays can be re-shaped manually:

```ipython
>>> x + y
ValueError: operands could not be broadcast together with shapes (2,3) (2,)

>>> x + y.reshape(2, 1)
array([[2., 2., 2.],
       [3., 3., 3.]])
```

## Boolean Arrays

Python's comparison operators have NumPy equivalents. They are applied to each
element and return a boolean array, indicating the result of every comparison:

| Shorthand | UFunc              | Description           |
|-----------|--------------------|-----------------------|
| `==`      | `np.equal`         | equal                 |
| `!=`      | `np.not_equal`     | not equal             |
| `<`       | `np.less`          | less than             |
| `>`       | `np.great`         | greater than          |
| `<=`      | `np.less_equal`    | less than or equal    |
| `>=`      | `np.greater_equal` | greater than or equal |

```python
>>> a = np.random.randint(1, 10, size=(3, 3))
>>> a
array([[3, 4, 6],
       [7, 4, 2],
       [3, 6, 5]])

>>> a == 5
array([[False, False, False],
       [False, False, False],
       [False, False,  True]])

>>> np >= 5
array([[False, False,  True],
       [ True, False, False],
       [False,  True,  True]])


>>> np.less(a, 5)
array([[ True,  True, False],
       [False,  True,  True],
       [ True, False, False]])
```

The number of true values can be counted using the `np.count_nonzero` or the
`np.sum` function, which counts `False` as 0 and `True` as 1. Using the array
`a` from above:

```python
>>> b = a >= 5
>>> b
array([[False, False,  True],
       [ True, False, False],
       [False,  True,  True]])

>>> np.count_nonzero(b)
4

>>> np.sum(b)
4

>>> np.count_nonzero(b, axis=0)
array([1, 1, 2])

>>> np.sum(b, axis=1)
array([1, 1, 2])
```

### Bitmasks

Boolean arrays can be used for indexing, where every `True` item of the index
array is returned:

```python
>>> x = np.random.randint(1, 100, size=(4, 4))
>>> x
array([[58, 26, 64,  3],
       [91, 64, 44, 31],
       [14, 81, 77,  8],
       [64, 42, 56, 37]])

>>> above_mean = (x > x.mean())
>>> above_mean
array([[ True, False,  True, False],
       [ True,  True, False, False],
       [False,  True,  True, False],
       [ True, False,  True, False]])

>>> x[above_mean]
array([58, 64, 91, 64, 81, 77, 64, 56])
```

Selection criteria can be combined using the bitwise operands, which are
shorthand for NumPy's element-wise logical UFuncs:

| Shorthand | UFunc            | Description  |
|-----------|------------------|--------------|
| `&`       | `np.bitwise_and` | and          |
| `\|`      | `np.bitwise_or`  | or           |
| `^`       | `np.bitwise_xor` | exclusive or |
| `~`       | `np.bitwise_not` | not          |

Using the arrays `x` and `above_mean` from above:

```python
>>> even = (x % 2 == 0)
>>> even
array([[ True,  True,  True, False],
       [False,  True,  True, False],
       [ True, False, False,  True],
       [ True,  True,  True, False]])

>>> x[even & above_mean]
array([58, 64, 64, 64, 56])

>>> x[np.bitwise_or(even, above_mean)]
array([58, 26, 64, 91, 64, 44, 14, 81, 77,  8, 64, 42, 56])

>>> odd = np.bitwise_not(even)
>>> odd
array([[False, False, False,  True],
       [ True, False, False,  True],
       [False,  True,  True, False],
       [False, False, False,  True]])
```

## Fancy Indexing

Arrays can be indexed using arrays of indices to access multiple array elements
at once. 
```python
>>> x = np.arange(5, 85, 5).reshape((4, 4))
>>> x
array([[ 5, 10, 15, 20],
       [25, 30, 35, 40],
       [45, 50, 55, 60],
       [65, 70, 75, 80]])

>>> x[[3, 1, 2], [2, 3, 1]] # select items (3,2), (1,3) and (2,1)
array([75, 40, 50])
```

### Broadcasting

If array indices with different shapes are used, the index arrays are being
broadcasted. The result of the index operation is shaped by the _broadcasted
index array_, not by the array being indexed. Given the array `x` from above:

```python
>>> rows = np.array([3, 1, 2])[:, np.newaxis)
>>> rows
array([[3],
       [1],
       [2]])

>>> cols = np.array([2, 3, 1]
>>> cols
array([2, 3, 1])

>>> x[rows, cols]
array([[75, 80, 70],
       [35, 40, 30],
       [55, 60, 50]])
```

The broadcasting of the index arrays is done like this:

|   | 2   | 3   | 1   |
|---|-----|-----|-----|
| 3 | 3,2 | 3,3 | 3,1 |
| 1 | 1,2 | 1,3 | 1,1 |
| 2 | 2,2 | 2,3 | 2,1 |

And the resulting array of the indexing operation looks like this:

|   | 2  | 3  | 1  |
|---|----|----|----|
| 3 | 75 | 80 | 70 |
| 1 | 35 | 40 | 30 |
| 2 | 55 | 60 | 50 |

Array indices can be combined with scalar indices, slicing and masking:

```python
>>> x[2, [1, 0, 3]] # scalar and array index
array([50, 45, 60])

>>> x[2:3, [1, 0, 3]] # slice and array index
array([50, 45, 60])

>>> rows = np.array([2, 3])[:, np.newaxis]
>>> cols = np.array([False, True, False, True])
>>> x[rows, cols] # array index and mask
array([[50, 60],
       [70, 80]])
```

### Assignment

Fancy indexing can be used for assignments, too:

```python
>>> x = np.arange(10)
>>> x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> x[x % 2 == 0] = 0 # set all even values to zero
>>> x
array([0, 1, 0, 3, 0, 5, 0, 7, 0, 9])
```

However, the behaviour can be unexpected if index values are used multiple
times:

```python
>>> x = np.zeros(3)
>>> x
array([0, 0, 0])

>>> i = [0, 1, 1, 2, 2, 2]
>>> x[i] += 1
>>> x
array([1, 1, 1])
```

The values at indices 1 and 2 haven't been incremented three times, because the
value of `x[i] + 1` is evaluated once at the beginning and then used multiple
times. For repetitions, NumPy's functions have a `at` method, which performs
unbuffered operations, i.e. results will be recalculated for every index
element:

```python
>>> x = np.zeros(3)
>>> x
array([0, 0, 0])

>>> i = [0, 1, 1, 2, 2, 2]
>>> np.add.at(x, i, 1)
>>> x
array([1, 2, 3])
```

## Sorting

NumPy offers more efficient ways of sorting arrays than Python's native
`sort()` function. An array can be sorted using the `np.sort()` function, which
returns the sorted array:

```python
>>> x = np.array([5, 2, 4, 1, 3])
>>> np.sort(x)
array([1, 2, 3, 4, 5])
```

By default, NumPy uses the quicksort algorithm. Other algorithms can be used by
setting the `kind` parameter. Options are: `quicksort`, `mergesort`, `heapsort`
and `stable`.

An array can also be sorted in-place, using the array's `sort()` method:

```python
>>> x = np.array([5, 2, 4, 1, 3])
>>> x.sort()
>>> x
array([1, 2, 3, 4, 5])
```

The `np.argsort()` function sorts an array and returns an array of indices
denoting the array's order. The returned array can be used for fancy indexing:

```python
>>> x = np.array([5, 2, 4, 1, 3])
>>> i = np.argsort(x)
>>> i
array([3, 1, 4, 2, 0])

>>> x[i]
array([1, 2, 3, 4, 5])
```

Arrays can be sorted along rows and columns using the `axis` argument, which
defines _along_ (_not within!_) which axis the comparison and swapping is
performed (0: along rows, 1: along columns):

```python
>>> x = np.random.choice(10, (3, 3), replace=False)
>>> x
array([[7, 1, 9],
       [8, 0, 4],
       [2, 3, 6]])

>>> np.sort(x, axis=0) # along rows/within columns
array([[2, 0, 4],
       [7, 1, 6],
       [8, 3, 9]])

>>> np.sort(x, axis=1) # along columns/within rows
array([[1, 7, 9],
       [0, 4, 8],
       [2, 3, 6]])
```

Arrays can be sorted _partially_, i.e. the array is split into two sections,
with the left partition containing all smaller values than the right partition.
Arrays can be sorted partially using `np.partition()`, which requires the `kth`
parameter denoting the size of the left partition (`K` elements):

```python
>>> x = np.random.choice(10, 10, replace=False)
>>> x
array([9, 1, 6, 0, 8, 5, 3, 2, 7, 4])

>>> np.partition(x, 3)
array([1, 0, 2, 3, 4, 5, 6, 7, 8, 9])
```

Within the partitions, the elements are in arbitrary order. Partial sorting can
also be done by row or column using the `axis` argument. To return the array of
partially sorted indices, the function `np.argpartition()` can be used
analogous to `np.argsort()`.

## Structured Arrays

Storing heterogeneous data, say names and wages of employees, in different
arrays of the same size is error prone: The relation of the data is not
obvious, and sorting the arrays mixes up the entries. NumPy offers structured
arrays, which can be defined with the `dtype` parameter using a compound data
type specification in three ways:

1) using the dictionary method, indicating the field names and formats
separately in two tuples:

```python
dtype={'names': ('name', 'age', 'salary'),
       'formats': ('U20', 'u1', 'f4')}
```

2) using a list of tuples, defining the field name and its type together in one
tuple per field:

```python
dtype=np.dtype([('name', 'U20'),
                ('age', 'u1'),
                ('salary', 'f4')])
```

3) without specifying the field names, using automatic names from `f0` to `fn`,
and defining the types as a comma-separated string:

```python
dtype=np.dtype('U20,u1,f4')
```

A type indicator consists of three parts:

1. the endianness (optional): `<` for little endian, `>` for big endian
    - `<f4`: little endian float of four bytes
    - `>i8`: big endian integer of eight bytes
2. the data type (see the next table)
3. the size of the field _in bytes_ (not in bits)

| Indicator      | Type              | Example | Equivalent              |
|----------------|-------------------|---------|-------------------------|
| `'b'`          | byte              | `'b'`   |                         |
| `'i'`          | signed integer    | `'i4'`  | `np.int32`              |
| `'u'`          | unsigned integer  | `'u1'`  | `np.uint8`              |
| `'f'`          | floating point    | `'f8'`  | `np.float64`            |
| `'c'`          | complex number    | `'c16'` | `np.complex128`         |
| `'S'` or `'a'` | string (ASCII)    | `'S5'`  |                         |
| `'U'`          | unicode string    | `'U10'` | `np.dtype(np.str_, 10)` |
| `'V'`          | raw data (`void`) | `'V'`   | `np.void`               |

The fields can be accessed by row, by column, by combining row and column, and
also using bit masks:

```python
>>> employees = np.zeros(3, dtype=np.dtype([('name', 'S10'), ('wage', 'f8')]))
>>> employees['name'] = ['Dilbert', 'Wally', 'Alice']
>>> employees['wage'] = [120000.00, 80000.00, 110000.00]
>>> employees
array([(b'Dilbert', 120000.),
       (b'Wally', 80000.),
       (b'Alice', 110000.)],
       dtype=[('name', 'S10'), ('wage', '<f8')])

>>> employees[employees['wage'] > 100000]]['name']
array([b'Dilbert', b'Alice'], dtype='|S10')
```

NumPy also allows storing arrays in fields of structured arrays, which can be
achieved by providing an optional size indicator to every field definition:

```python
>>> players = np.zeros(3, dtype=np.dtype([('name', 'U20'),
                                          ('pattern', 'S1', (3, 3))]))
>>> players[0]['name'] = 'John'
>>> glider = [[' ', 'O', ' '],
              [' ', ' ', 'O'],
              ['O', 'O', 'O']]
>>> players[0]['pattern'] = glider
```

NumPy offers the type `np.recarray`, which allows the individual fields to be
accessed with dot notation instead of array indices:

```python
>>> payroll = employees.view(np.recarray)
>>> payroll.name
array([b'Dilbert', b'Wally', b'Alice'], dtype='|S10')
```

The syntax is more convenient, but the performance of the access is lower.

NumPy's structured arrays are a very efficient way to store structured data.
However, the Pandas library offers much more functionality for working with
structured data.
