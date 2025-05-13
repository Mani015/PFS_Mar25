
# Check a number perfect number or not ?

# 6 : 1,2,3 1 + 2 + 3 = 6
# 28:  1,2,4,7,14 



num = int(input('Enter a number : '))

perfect_num = 0
for i in range(1,num):

	if num % i == 0:

		perfect_num = perfect_num + i


print('perfect number' if perfect_num == num else 'Not a Perfect Number')

# Enter a number : 6
# perfect number

# Enter a number : 10
# Not a Perfect Number


# Enter a number : 28
# perfect number