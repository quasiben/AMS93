"""
we're going to plot a moving timeseries

First, we need to generate a random walk.

1.  Use numpy to generate a random walk of length 100.
I would do this by using np.random.randn to generate
some standard normals, and center it to 1
and then divide it by 1000.0 to
make the vol small.

2.  Taking np.cumprod of the resulting array
should give you a random walk.

3.  plot the line, make sure you assign the resulting line object
to some variable in the python namespace

4.  Loop over some range (say range(20)).
At every step, discard the first value in the array,
and add a new value to the random walk.
then call set_ydata on the line, and call draw.
sleep for 0.2 seconds
"""

import numpy as np
import pylab
import time

data = 1 + np.random.randn(100) / 1000.0
data = np.cumprod(data)
line = pylab.plot(data)[0]

for c in range(100):
    newval = data[-1] * ( 1 + np.random.randn(1) / 1000.0)
    data = np.concatenate((data[1:], newval))
    line.set_ydata(data)
    pylab.draw()
    time.sleep(0.2)
