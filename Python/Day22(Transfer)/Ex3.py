# Duck Number ?
# A number which contains zero, shouldn't starts with 0
# Ex : 123045 --> Duck number
# Ex : 02345  --> Not a Duck number


num = int(input('Enter the number : '))


is_duck = False

while num != 0:   # 123045

	digit = num % 10   # Takes remainder value

	if digit == 0:
		is_duck = True
		break

	num = num // 10


if is_duck:
	print('Duck number')

else:
	print('Not a DUck number')


# Enter the number : 234056
# Duck number


# Enter the number : 098765
# Not a DUck number



# continue Skip the current iteration of a loop and move to the next iteration
# pass	Do nothing. Ignore the condition in which it occurred and proceed to run the program as usual