
Name = "Suresh"
print(f'Global var : {Name}')
def Personal_info():

	global Name
	Name  = "yogeswar"

	print(f'Candidate : {Name}')



Personal_info()

print(f'Global var : {Name}')

# Global var : Suresh
# Candidate : yogeswar
# Global var : yogeswar

