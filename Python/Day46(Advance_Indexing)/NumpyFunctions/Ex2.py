# Zeros: Return a new array of given shape and type, filled with zeros.
import numpy as np

# print(help(np.zeros))
# zeros_like : Return an array of zeros with shape and type of input.
#     empty : Return a new uninitialized array.
#     ones : Return a new array setting values to one.

z1 = np.zeros(3,dtype='int')
# print(z1)

z2 = np.zeros((3,2),dtype='int')
# print(z2)
#  [[0 0]
#  [0 0]
#  [0 0]]

# print(help(np.empty))
# Return a new array of given shape and type, without initializing entries.

e1 = np.empty(3)
# print(e1)
# [4.94065646e-324 6.95332925e-310 6.95332924e-310]
e2 = np.empty((4,5),dtype='int')
print(e2)
# [[ 813382954 2055025196 1852788246 1935761965  540292709]
#  [1768384868 1868963956  694447733    2322955  695336960]
#  [1912602624         42      11122    2912768  762445824]
#  [-637534208 -630885886 1819633161 1952542060  661809251]]
