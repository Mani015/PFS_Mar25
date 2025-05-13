
# What is a Spy number ?
#    Hint :if the sum of digits is exactly equals to the Product of digit , particular number is known as a SPY number.
#    Ex : 1421 
#    sum = 1+4+2+1 = 8
#    pro = 1*4*2*1 = 8


num = 1421

sum_of_num = 0
product_of_num = 1

while num != 0:

	digit = num % 10
	# sum of numbers with digit
	sum_of_num = sum_of_num + digit

	#product of numbers with digit
	product_of_num = product_of_num * digit

	num = num // 10



print('Spy number' if sum_of_num == product_of_num else "Not a Spy number")








