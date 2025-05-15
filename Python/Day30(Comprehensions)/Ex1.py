
# List comprehension : List comprehension is a shorter syntax, to create a new list based an existing list.

# sy : [Expression for value in Sequence]

# Execute 1st 10 number in list

# print([num for num in range(1,11)])


# print([i+1 for i in range(1,11)])
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print()
# print([k for k in range(1,21) if k % 2 == 0])
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# sy : [expression if condition else statement for value in sequence]

l1 = [9,10,8,7,5,6,3,4,2,1]
l2 = []
for i in l1:
    if i % 2 == 0:
        l2.append(i-1)
    else:
        l2.append(i)

# print(l2)
# [9, 9, 7, 7, 5, 5, 3, 3, 1, 1]


print([a-1 if a % 2 == 0 else a for a in l1])