# Creating two dimensional Array
import numpy as np

a1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(a1)
# print('shape of array :', a1.shape)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
# a2 = a1.reshape(5,4)
# print()
# print(a2)

rows = int(input('Enter no.of rows :'))
columns = int(input('Enter no.of Columns :'))
a2 = np.ndarray(shape=(rows,columns),dtype=int)

print('Enter total elements : ', rows * columns)
for row in range(rows):  # for row in range(3)
    for col in range(columns):   # for col in range(4)
        a2[row][col] = int(input('Enter element :'))
print(a2)
# Enter no.of rows :5
# Enter no.of Columns :4
# Enter total elements :  20
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]


# 4X4 matrix
# [[ 11  22  33  44]
#  [ 55  66  77  88]
#  [ 99 100 111 222]
#  [333 444 555 666]]
