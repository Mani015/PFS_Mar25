
# check a number even or odd using lambda  function

# print((lambda x : 'even num' if x% 2 == 0 else 'Odd number')(int(input('enter a number : '))))
# enter a number : 12
# even num



l1 = []

for i in range(1,6):
    for j in range(1,6):
        l1.append((i,j))

# print(l1)
# [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1),
# (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 1), (5, 2), (5, 3),
# (5, 4), (5, 5)]



print(list(set([sum((i,j,k)) for i in range(1,6) for j in range(1,6) for k in range(6,11)])))
