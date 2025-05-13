
# extend : adding more than one value to the list

prime_num : list[int] = [2,3,5,7,9,11,13]
print(prime_num)
# [2, 3, 5, 7, 9, 11, 13]


# sy : list.extend(object)

prime_num.extend([17,19])

print(prime_num)
# [2, 3, 5, 7, 9, 11, 13, 17, 19]

prime_num.extend((23,26,27))

print(prime_num)
# [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 26, 27]

