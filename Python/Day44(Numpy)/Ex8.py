import numpy as np
# 3-dimensional array, which is 2-d present in that
n3 = np.array([
    [
        [10,11,12,13],
        [14,15,16,17],
        [18,19,20,21]
    ],

    [
        [22,23,24,25],
        [26,27,28,29],
        [30,31,32,33]
    ]

    ])

# 3-d slice
#              k      ,        l           ,        m
# [start : stop : step, start : stop : step, start : stop : step]

# print(n3[0])

x = n3[0 : :, 0 : 1 : ,  : :  ]
print(x)
# [[[10 11 12 13]]
#
#  [[22 23 24 25]]]


