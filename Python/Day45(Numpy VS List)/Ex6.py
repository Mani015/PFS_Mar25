# What is an Array ?
# An array is basically a data structure which can be holds more than one value at a time.
# It is a collection or ordered series of elements of the same type


# Difference between numpyArray and list

# By default arrays concept is not available in python , instead of we can use list.
# [But, make sure list and Arrays both are not same]

# 1.But in python , we can create arrays in the following 2 ways
# How to import module?
# 1. By using array module
# 2. By using numpy Module


# 1. By using array module
import array
a1 = array.array('i',[1,2,3,4,5])
# print(type(a1))
# print(a1)
# <class 'array.array'>
# array('i', [1, 2, 3, 4, 5])

# 2. By using numpy Module
import numpy as np

n1 = np.array([10,12,13,14,15])
print(type(n1))
print(n1)
# # 2. By using numpy Module
