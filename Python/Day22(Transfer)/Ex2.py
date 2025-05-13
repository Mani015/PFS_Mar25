

start = int(input('Enter start number : '))

stop = int(input('Enter stop number : '))

First_7_even_num = 0

for i in range(start,stop):

	if i % 2 == 0:

		First_7_even_num = First_7_even_num + 1
		print(f'{i} is an even number')

		if First_7_even_num == 7:
			break


else:
	print("Sorry break didn't work ")

print('No of even numbers : ', First_7_even_num)

# Enter start number : 24
# Enter stop number : 45
# 24 is an even number
# 26 is an even number
# 28 is an even number
# 30 is an even number
# 32 is an even number
# 34 is an even number
# 36 is an even number
# No of even numbers :  7