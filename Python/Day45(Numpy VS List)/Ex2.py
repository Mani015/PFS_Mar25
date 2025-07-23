# Creating two dimensional Array

# rows = int(input('Enter no.of rows :'))
# columns = int(input('Enter no.of Columns :'))

# print(help(np.ndarray))
# class ndarray(builtins.object)
#  |  ndarray(shape, dtype=float, buffer=None, offset=0,
# #  |          strides=None, order=None)
# import numpy as np
# a1 = np.ndarray(shape=[10],dtype=int)  # ndarray object it will take float value as by defaulty
# print(a1)
#[         0          1          1 1936291698 1752440933 1701978213
 # 1852994932  537551973  538976288 1629495328]



# quit()

# Creating two dimensional Array

import numpy as np
rows = int(input('Enter no.of rows :'))
columns = int(input('Enter no.of Columns :'))

array_list = np.ndarray(shape=(rows,columns),dtype=int)
print('Size of array: ',array_list.size)
print('Shape of array :', array_list.shape)
print('dimension array :', array_list.ndim)
# Enter no.of rows :5
# Enter no.of Columns :4
# Size of array:  20
# Shape of array : (5, 4)
# dimension array : 2
