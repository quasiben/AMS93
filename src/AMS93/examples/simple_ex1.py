"""
generate 2 random walks in a matrix
"""
import numpy as np
data = 1 + np.random.randn(10000, 2)/1000.0
data = np.cumprod(data, axis=0)
"""
plot lines of both 
"""
pylab.plot(data)

"""
plot column one using red circles, and column 2 using black circles
"""
x = np.arange(len(data))
pylab.plot(x, data[:,0], 'ro', x, data[:, 1], 'ko')

"""
create a scatter plot of column 2 vs column 1
"""
pylab.plot(data[:,0], data[:, 1]  'ro')

