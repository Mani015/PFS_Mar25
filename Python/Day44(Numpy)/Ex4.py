
import numpy as np

n2  = np.array([[11,12,13],[14,15,16],[17,18,19],[20,21,22]])
# print(n2)
# [[11 12 13]
#  [14 15 16]
#  [17 18 19]
#  [20 21 22]]

# print('Size : ', n2.size)  # size is not an object default variable
# print('Shape: ', n2.shape)
# print('Ndimensions :', n2.ndim)
# print('Item size : ',n2.itemsize)
# print('Data type :', n2.dtype)
# print('Bytes : ',n2.nbytes)

# Size :  12
# Shape:  (4, 3)
# Ndimensions : 2
# Item size :  4
# Data type : int32
# Bytes :  48

# reshape the array
n3 = n2.reshape(3,4)
# print(n3)

# print('Size : ', n3.size)  # size is not an object default variable
# print('Shape: ', n3.shape)
# print('Ndimensions :', n3.ndim)
# print('Item size : ',n3.itemsize)
# print('Data type :', n3.dtype)
# print('Bytes : ',n3.nbytes)

# [[11 12 13 14]
#  [15 16 17 18]
#  [19 20 21 22]]
# Size :  12
# Shape:  (3, 4)
# Ndimensions : 2
# Item size :  4
# Data type : int32
# Bytes :  48


print()
print(n2.reshape(6,2),'6X2')
# [[11 12]
#  [13 14]
#  [15 16]
#  [17 18]
#  [19 20]
#  [21 22]] 6X2

