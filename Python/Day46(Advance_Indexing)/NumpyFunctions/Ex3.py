
# Ones :Return a new array of given shape and type, filled with ones.
import numpy as np
# print(help(np.ones))
# sy:  ones(shape, dtype=None, order='C', *, like=None)

# print(help(np.linspace))
#
# linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
#     Return evenly spaced numbers over a specified interval.

# num : int, optional
#         Number of samples to generate. Default is 50. Must be non-negative.
l1 = np.linspace(100,105)  # Default num is 50
# print(l1)
# [100.         100.10204082 100.20408163 100.30612245 100.40816327
#  100.51020408 100.6122449  100.71428571 100.81632653 100.91836735
#  101.02040816 101.12244898 101.2244898  101.32653061 101.42857143
#  101.53061224 101.63265306 101.73469388 101.83673469 101.93877551
#  102.04081633 102.14285714 102.24489796 102.34693878 102.44897959
#  102.55102041 102.65306122 102.75510204 102.85714286 102.95918367
#  103.06122449 103.16326531 103.26530612 103.36734694 103.46938776
#  103.57142857 103.67346939 103.7755102  103.87755102 103.97959184
#  104.08163265 104.18367347 104.28571429 104.3877551  104.48979592
#  104.59183673 104.69387755 104.79591837 104.89795918 105.        ]

# endpoint : bool, optional
#         If True, `stop` is the last sample. Otherwise, it is not included.
#         Default is True.
l2 = np.linspace(1,10,num=10)
# print(l2)
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

l3 = np.linspace(1,10,num=10,endpoint=False)
# print(l3)
# [1.  1.9 2.8 3.7 4.6 5.5 6.4 7.3 8.2 9.1]


# retstep=False

l4 = np.linspace(1,10,retstep=True,num=100)
print(l4)
# (array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]), 1.0)
