# Matplotlib

Matplotlib is a multiplatform data visualization library built on NumPy arrays.
It supports different graphic backends and output styles, and works on
virtually any platform. Some projects, including Pandas, offer wrappers around
the API of Matplotlib. It is, however, still useful to know how to deal
directly with Matplotlib.

Conventionally, Matplotlib is imported as follows:

```python
>>> import matplotlib as mpl
>>> import matplotlib.pyplot as plt
```

The plot style can be set on the `plt` object:

```python
>>> plt.style.use('classic')
```

Depending on the context, there are different ways of opening the plots for
display.

From a script, the method `plt.show()` opens all figures plotted so far:

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()
```

The method `plt.show()` must onle be used once per script or session.

Plots created in a IPython shell can be displayed automatically by calling the
`%matplotlib` magic command before calling methods on the `plt` object. The
plot will be displayed in a separate window. The method `plt.draw()` forces the
output to be updated.

```python
>>> import matplotlib as mpl
>>> import matplotlib.pyplot as plt
>>> import numpy as np

>>> %matplotlib
Using matplotlib backend: Qt5Agg

>>> x = np.linspace(0, 10, 100)
>>> plt.plot(x, np.sin(x))
```

From within a Jupyter Notebook, there are two options to display plots:

1. `%matplotlib inline`: display plots as static images
2. `%matplotlib notebook`: display interactive plots

The latter option will draw every plot output in the most recent figure, which
can be created using the `plt.figure()` method:

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

%matplotlib notebook

plt.figure()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
```

A figure object can be saved using its `savefig()` method, which requires a
file name. Notice that the `plot()` method only draws into the most recent
figure object created, if the magic command `%matplotlib` hasn't been used
before:

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
fig.savefig('sin-x-cos-x.png')
```

![Plot of `sin(x)` and `cos(x)`](plots/sin-x-cos-x.png)

An image--no longer a plot!--can be loaded using IPython's `Image` object:

```python
>>> from IPython.display import Image, display
>>> img = Image('sin-x-cos-x.png')
>>> display(img)
```

For both saving and loading, the file format is inferred from the file's
extension. The formats supported by the graphics backend in use can be
retrieved as a dictionary from a `figure` object:

```python
>>> import matplotlib as mpl
>>> import matplotlib.pyplot as plt

>>> fig = plt.figure()
>>> fig.canvas.get_supported_filetypes()
{'ps': 'Postscript',
 'eps': 'Encapsulated Postscript',
 'pdf': 'Portable Document Format',
 'pgf': 'PGF code for LaTeX',
 'png': 'Portable Network Graphics',
 'raw': 'Raw RGBA bitmap',
 'rgba': 'Raw RGBA bitmap',
 'svg': 'Scalable Vector Graphics',
 'svgz': 'Scalable Vector Graphics'}
```

## Interfaces: MATLAB-style and Object Oriented

Matplotlib started out as a Python alternative for MATLAB. The `plt` object
represents the stateful interface known to MATLAB users. Plots created on the
`plt` object are drawn to the figure and axes objects that have been created
most recently.

In this example, two subplots on a single figure are created:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.figure() # create a new figure
plt.subplot(2, 1, 1) # (row, column, panel): first panel on a 2*1 field
plt.plot(x, np.sin(x)) # plot to the first subplot
plt.subplot(2, 1, 2) # second panel on the same 2*1 field
plt.plot(x, np.cos(x)) # plot to the second subplot
plt.show()
```

![MATLAB-style interface: Subplots](plots/matlab-style-1.png)

It is possible to plot on other figures/axes than the current active, but only
if their references have been retrieved and stored using `plt.gcf()` (get
current figure) and `plt.gca()` (get current axes):

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))
first = plt.gca() # store reference to first aces
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
first.plot(x, np.cos(x)) # also draw cosine on first axes
plt.show()
```

![MATLAB-style interface: Draw to "inactive" Axes](plots/matlab-style-2.png)

"Going back" is not possible if one fails to store the such references,
especially in an interactive session. The object-oriented interface of
Matplotlib doesn't rely on a _current state_, but requires the user to always
explicitly refer to the figure/axes to be dealt with:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(2)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
ax[0].plot(x, np.cos(x))
plt.show()
```

The choice between the two interfaces is mostly a matter of preference for
simple tasks. More complicated plots, however, do require the object-oriented
approach.
