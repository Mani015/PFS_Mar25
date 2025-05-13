l1 = [3,4,7,9,5,2,2,5,7,9,10,12,89,45,23,42]

# Using the above list , find out the sum of even & odd numbers with out using in-built method



sum_of_even = 0
sum_of_odd = 0

for num in l1:

	if num % 2 == 0:
		sum_of_even = sum_of_even + num


	else:
		sum_of_odd = sum_of_odd + num

print(f'Sum of even num : {sum_of_even}')
print(f'Sum of odd num : {sum_of_odd}')

# Sum of even num : 72
# Sum of odd num : 202
