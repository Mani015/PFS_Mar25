
name = ['reddy','pragathi','trupti','viswa']
age = [11,22,33,44]

name_age = list(zip(name,age))
print(f'name - age : {name_age}')

quit()

l1 = [1,2,3,4,5,6,7,8]
# print(l1+2)
# (1+2),(2+2),(3+2)
# TypeError: can only concatenate list (not "int") to list

import array
a1 = array.array('i',[1,2,3,4,5])
a2 = array.array('i',[2,3,4,5,6])
# print(a1+a2)  Dot product
# (1*2) + (2*3) + (4*3) + (4*5) + (5*6)
# print(a1[0]*a2[0] + a1[1]*a2[1])
# Normal Python


def Product_Operation(a,b):
    result = 0
    for v1,v2 in zip(a,b):
        result = result + v1 * v2
    print('The final Result :',result)
# Product_Operation(a1,a2)
#The final Result : 70


import numpy as np

d1 = np.dot(a1,a2)
print('FInal Result : ', d1)
# FInal Result :  70



