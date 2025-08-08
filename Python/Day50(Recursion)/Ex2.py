


import sys

sys.setrecursionlimit(300)

g1 = 0

def Recursive():

    global g1
    g1+=1
    print(f'calling : {g1}')
    Recursive()

Recursive()