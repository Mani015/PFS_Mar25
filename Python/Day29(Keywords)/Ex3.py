
# without keyword

# def DOMS1():

# 	Marker = 'Blue'
# 	print(f'currently enscope var : {Marker}')

# 	def DOMS2():

# 		Marker = 'Black'
# 		print(f'Local variable : {Marker}')

# 	DOMS2()
# 	print(f'After enscope var : {Marker}')

# DOMS1()

# currently enscope var : Blue
# Local variable : Black
# After enscope var : Blue



# With keyword (nonlocal keyword used in local scope)

def DOMS1():

	Marker = 'Blue'
	print(f'currently enscope var : {Marker}')

	def DOMS2():

		nonlocal Marker
		Marker = 'Black'
		print(f'Local variable : {Marker}')

	DOMS2()
	print(f'After enscope var : {Marker}')

DOMS1()

# currently enscope var : Blue
# Local variable : Black
# After enscope var : Black
