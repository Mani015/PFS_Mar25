
# Slicing 1-Dimension :

import numpy as np

n1 = np.array([1,2,3,4,5,6,7,8,9,10])
# print(n1)
# [ 1  2  3  4  5  6  7  8  9 10]

# syntax : [start : stop : step]


# 2-D slicing
#                 rows     ,      columns
# sy : [start : stop : step, start : stop : step]

n2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(n2)
#     c0 c1 c2  c3
# [r0[ 1  2  3  4]
#  r1[ 5  6  7  8]
#  r2[ 9 10 11 12]
#  r3[13 14 15 16]]

# [1 2 3 4]
# [5 6 7 8]
print()
x = n2[0 : 2, : : ]
print(x)
# [[1 2 3 4]
#  [5 6 7 8]]


