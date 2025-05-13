

l1 = [6,5,2,4,6,9,8,4,2,3,56,7,9,0,8,4,1,2,45,6,8,9,10]

Unique_list = []


for value in l1:

	if value not in Unique_list:

		Unique_list.append(value)


print(Unique_list)
# [6, 5, 2, 4, 9, 8, 3, 56, 7, 0, 1, 45, 10]
