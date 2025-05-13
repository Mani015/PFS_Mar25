
is_prime = 0
print('intially is_prime value : ',is_prime)

num = int(input('Enter a number : '))


for i in range(1,num+1):

	if num % i == 0:  # 7 %1 == 0, 7 % 7 == 0

		is_prime = is_prime + 1

print('currently is_prime value : ', is_prime)

if is_prime == 2:

	print('Prime number')


else:

	print('Not a prime number')
