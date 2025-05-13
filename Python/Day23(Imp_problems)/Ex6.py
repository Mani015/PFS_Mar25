

start = int(input('Enter the start number : '))

stop = int(input('Enter the stop number : '))


for num in range(start,stop+1):

	for var in range(2,num):

		if num % var == 0:

			break


	else:

		print('Prime number : ', num)




