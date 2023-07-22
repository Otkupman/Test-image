# -*- coding: utf-8 -*-
"""
A code fragment, using the Python programming language as an example, may look as follows

@author: Otkupman D.G.
"""

import numpy as np	# Importing a library for working with arrays

lim_min = int() # Minimum limit
lim_max = int() # Maximum limit

step = float() # Step
const = float() # Some constant

points = np.arange(lim_min, lim_max, step) # Array creation

xs, ys = np.meshgrid(points, points) # List of arrays of coordinate grids of N-dimensional coordinate space

z = np.sqrt(np.square(xs) + np.square(ys)) # Formula (example for a circle)

image = np.where(z>const, 0, 255) # Definition of thresholds