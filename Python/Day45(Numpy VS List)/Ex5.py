
import numpy as np
from datetime import datetime

a = np.array([1,2,3,4,5])
b = np.array([10,20,30,40,50])


def Dot_function(a,b):
    result = 0
    for i,j in zip(a,b):
        result = result + i * j
    return result

start = datetime.now()
for i in range(100000):
      Dot_function(a,b)
end = datetime.now()

print('The Normal python time taken : ', end-start)
print()
# quit()
start = datetime.now()

for i in range(100000):
    np.dot(a,b)
end = datetime.now()
print('The numpy module time taken : ', end-start)

# The Normal python time taken :  0:00:00.330452
# The numpy module time taken :  0:00:00.272005


quit()
l1 = [1,2,3,4,5,6,7,8]
# print(l1+2)
# (1+2),(2+2),(3+2)
# TypeError: can only concatenate list (not "int") to list

import array
a1 = array.array('i',[1,2,3,4,5])
a2 = array.array('i',[2,3,4,5,6])
# Normal Python
from datetime import datetime
def Product_Operation(a,b):
    result = 0
    for v1,v2 in zip(a,b):
        result = result + v1 * v2
    return result
start_time = datetime.now()
for i in range(1000000):
      Product_Operation(a1,a2)
end_time = datetime.now()
print('Normal Python time taken :', end_time - start_time)
#The final Result : 70
print()
# Normal Python time taken : 0:00:00.122356
# quit()
import numpy as np
start_time1 = datetime.now()
for i in range(1000000):
    np.dot(a1,a2)
end_time1 = datetime.now()
# print('FInal Result : ', d1)
# FInal Result :  70
print('Numpy module time taken :', end_time1 - start_time1)



