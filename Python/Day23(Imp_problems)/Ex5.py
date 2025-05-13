
# Check a wheater is it prime number or not ?


# num = int(input('Enter a number : '))


# valid_num = 0

# for i in range(1,num + 1):  # (1,5 + 1)

# 	if num % i == 0:  # 5 % 1 == 0, 5 % 2, 5 % 3, 5 % 4, 5 % 5 == 0

# 		valid_num = valid_num + 1


# if valid_num == 2:

# 	print(f'{num} is a Prime number')


# else:

# 	print(f'{num} is not a prime number')


# Enter a number : 3
# 3 is a Prime number


# Enter a number : 10
# 10 is not a prime number



All_num = [10,23,5,6,8,3,12,17,34,29,50,7]

prime_list = []


for i in All_num:

	for j in range(2,i):

		if i % j == 0:
			
			break

	else:
		prime_list.append(i)

print(prime_list)


# [23, 5, 3, 17, 29]






# for i in range(1,6):
# 	for j in range(1,4):
# 		print(f'i repeats : {i} , j repeats : {j} ')

# 	print()


# i repeats : 1 , j repeats : 1 
# i repeats : 1 , j repeats : 2 
# i repeats : 1 , j repeats : 3 

# i repeats : 2 , j repeats : 1 
# i repeats : 2 , j repeats : 2 
# i repeats : 2 , j repeats : 3 

# i repeats : 3 , j repeats : 1 
# i repeats : 3 , j repeats : 2 
# i repeats : 3 , j repeats : 3 

# i repeats : 4 , j repeats : 1 
# i repeats : 4 , j repeats : 2 
# i repeats : 4 , j repeats : 3 

# i repeats : 5 , j repeats : 1 
# i repeats : 5 , j repeats : 2 
# i repeats : 5 , j repeats : 3 



