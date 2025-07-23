# eye :
import numpy as np
# print(help(np.eye))
# eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None)
#     Return a 2-D array with ones on the diagonal and zeros elsewhere.
#

# N : int
#       Number of rows in the output.
#     M : int, optional
#       Number of columns in the output. If None, defaults to `N`.
#     k : int, optional
#       Index of the diagonal: 0 (the default) refers to the main diagonal,
#       a positive value refers to an upper diagonal, and a negative value
#       to a lower diagonal.


e1 = np.eye(2,dtype='int')
# print(e1)
# [[1 0]
#  [0 1]]

e2 = np.eye(3,4,dtype='int',k=-2)
print(e2)
# [[1 0 0 0]
#  [0 1 0 0]
#  [0 0 1 0]]


