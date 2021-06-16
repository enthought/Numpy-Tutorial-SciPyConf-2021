"""
Sinc Function
-------------

Topics: Broadcasting, Fancy Indexing

Calculate the sinc function: sin(r)/r.  Use a Cartesian x,y grid
and calculate ``r = sqrt(x**2+y**2)`` with 0 in the center of the grid.
Calculate the function for -15,15 for both x and y.

See :ref:`sinc-function-solution`.
"""

from numpy import linspace, sin, sqrt, newaxis
import matplotlib.pyplot as plt
