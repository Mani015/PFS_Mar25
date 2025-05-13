
l1 = [3,4,7,9,5,2,2,5,7,9,10,12,89,45,23,42]

even_list = []
odd_list = []

for i in l1:

	if i % 2 == 0:

		even_list.append(i)

	else:

		odd_list.append(i)


print(even_list)
print(odd_list)

# [4, 2, 2, 10, 12, 42]
# [3, 7, 9, 5, 5, 7, 9, 89, 45, 23]
