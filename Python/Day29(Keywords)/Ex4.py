

def Universe1():

	global Light

	Light  = 'Moon'

	print(f'Enclose var : {Light}')


	def Universe2():

		global Light

		Light = 'Sun'

		print(f'Local var : {Light}')


	Universe2()
	print('enclosing var : ',Light)

Universe1()

print('Global var : ',Light)

# Enclose var : Moon
# Local var : Sun
# enclosing var :  Sun
# Global var :  Sun