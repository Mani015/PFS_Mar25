import numpy as np

# print(help(np.arange))
# arange([start,] stop[, step,], dtype=None, *, like=None)
# np.arange(0, 5, 0.5, dtype=int)
#       array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#       >>> np.arange(-3, 3, 0.5, dtype=int)
#       array([-3, -2, -1,  0,  1,  2,  3,  4,  5,  6,  7,  8])

# a1 = np.arange(10)
# print(a1)
# [0 1 2 3 4 5 6 7 8 9]

a1 = np.arange(10,dtype='float32')
# print(a1)
# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

a2 = np.arange(1,10,0.5)
# print(a2)
# [1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5 8.  8.5 9.  9.5]


a3 = np.arange(1,11.5)
print(a3)
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11.]
