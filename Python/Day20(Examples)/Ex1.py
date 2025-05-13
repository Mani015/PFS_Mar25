num = [1,2,-9,8,-7,6,3,-5,4,10,12,-4,13]

# Store into a different lists  +ve & -ve numbers

positive_num = []

negative_num = []

for i in num:

	if i > 0:
		positive_num.append(i)

	else:

		negative_num.append(i)

print('+ve  : ',positive_num)
print('-ve  : ',negative_num)

# +ve  :  [1, 2, 8, 6, 3, 4, 10, 12, 13]
# -ve  :  [-9, -7, -5, -4]





