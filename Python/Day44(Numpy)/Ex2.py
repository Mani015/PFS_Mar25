
# Les's the properties of Numpy.


import numpy as np

n2 = np.array([1,2,3,4,5,6,7,8,9,10])
print(n2)
# [ 1  2  3  4  5  6  7  8  9 10]

print(f'N dimensions of  : {n2.ndim}')
# N dimensions of  : 1
print(f'Datatype : {n2.dtype}')
# Datatype : int32

print(f'Size is : {n2.size}')
# Size is : 10

print(f'shape is : {n2.shape}')  # shape(rows,col)
# shape is : (10,)


print(help(np.array))
