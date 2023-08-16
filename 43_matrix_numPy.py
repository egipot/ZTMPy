#https://www.delftstack.com/howto/numpy/python-numpy-print-full-array/
#https://numpy.org/doc/stable/user/absolute_beginners.html


#this code runs successfully in Anaconda prompt (Anaconda3) python
import sys
import numpy as np
array = np.arange(101)
np.set_printoptions(threshold=sys.maxsize)
print(array)

