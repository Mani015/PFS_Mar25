# Chain multiple if statement in Python
# In Python, the if-elif-else condition statement has an elif blocks to chain multiple conditions one after another.
#  This is useful when you need to check multiple conditions.

a=33
b=33
if b>a:
	print(b,'is greater than',a)
elif b==a:
	print(f'{a} is equal to {b}')
else:
	print(f'{a} is not equal to {b}')