# Advance Indexing.

l1 = [1,2,3,4,5,6,7,8]

ind = [0,2,3,5]
# print(l1[ind])
# TypeError: list indices must be integers or slices, not list

import numpy as np
import array
n1 = np.array([11,22,33,44,55,66,77,88,99])

# orbitary elements : means of they don't have proper order
# 11,33,44,66,99

index = array.array('i',[0,2,3,5,8])

print(n1[index])
# [11 33 44 66 99]



