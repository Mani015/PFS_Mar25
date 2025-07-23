# 2-Dimensional Array

import numpy as np

n1 = np.array([[1,2,3,4],[5,6,7,8]])
# print(n1)

# [r0[1 2 3 4]
#  r1[5 6 7 8]]

# properties

print('Size : ', n1.size)  # size is not an object default variable
print('Shape: ', n1.shape)
print('Ndimensions :', n1.ndim)
print('Item size : ',n1.itemsize)
print('Data type :', n1.dtype)
print('Bytes : ',n1.nbytes)

# Size :  8
# Shape:  (2, 4)
# Ndimensions : 2
# Item size :  4
# Data type : int32
# Bytes :  32


# index of 0
print(n1[0])
print(n1[1])

# [1 2 3 4]
# [5 6 7 8]
print(n1[0][0])



