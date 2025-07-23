
import numpy as np

a1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(a1)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

# print(a1.reshape(5,2))
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]]

# T : Transpose
# print(a1.T)
# [[ 1  6]
#  [ 2  7]
#  [ 3  8]
#  [ 4  9]
#  [ 5 10]]

a2 = a1.T
# print(a2)
# print('shape of :',a2.shape)
# print('ndim:',a2.ndim)
# shape of : (5, 2)
# ndim: 2


# print(help(np.random))
# rand                 Uniformly distributed values.
#     randn                Normally distributed values.
#     ranf                 Uniformly distributed floating point numbers.
#     random_integers      Uniformly distributed integers in a given range.
#                          (deprecated, use ``integers(..., closed=True)`` instead)
#     random_sample        Alias for `random_sample`
#     randint              Uniformly distributed integers in a given range
#     seed                 Seed the legacy random number generator.


n1 = np.random.randn(10)
# print(n1)
# [ 0.43358099 -0.03823752 -1.84773229  0.93149836  0.24956039  0.52271878
#   0.07315913 -1.72923219 -1.70458323 -1.22376207]
print()
n2 = np.random.ranf(5)
print(n2)
# [0.87535159 0.63455045 0.32120048 0.05670491 0.35986488]
print()
s1 = np.random.set_bit_generator(12345)
# print(s1)