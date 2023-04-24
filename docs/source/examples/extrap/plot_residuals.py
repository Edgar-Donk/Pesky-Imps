# https://stackoverflow.com/questions/51220918/python-plot-residuals-on-a-fitted-model
'''
First of all note that axvline here only works by coincidence. In general the y
values taken by axvline are in coordinates relative to the axes, not in data
coordinates.

In contrast, vlines uses data coordinates and also has the advantage to accept
arrays of values. It will then create a LineCollection, which is more efficient
than individual lines.
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.2,1.2,20)
y = np.sin(x)
dy = (np.random.rand(20)-0.5)*0.5

fig, ax = plt.subplots()
ax.plot(x,y)
ax.scatter(x,y+dy)

ax.vlines(x,y,y+dy)

plt.show()