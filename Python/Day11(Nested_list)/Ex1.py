
# Nested list.
# A list inside of another lists is called nested list.

#          0,      1   ,    2  ,     3
#        ------ ,----- , ----- ,  -------
#        0,1,2   0,1,2   0,1,2    0, 1, 2
l1   = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

# Extract [1,2,3]
# print('index of 0 :', l1[0])
# print('index of 1 :', l1[1])
# print('index of 2 :', l1[2])
# print('index of 3 :', l1[3])
# index of 0 : [1, 2, 3]
# index of 1 : [4, 5, 6]
# index of 2 : [7, 8, 9]
# index of 3 : [10, 11, 12]


# Extract 1
print('index of 0 of 0 :', l1[0][0])
# index of 0 of 0 : 1

print('index of 0 of 1:', l1[0][1])
# index of 0 of 1: 2



