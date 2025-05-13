
Stu = {
	'Name' : 'Santhosh',
	'Age' : 20,
	'Country' : 'India',
	'Marks' : 100,
	'Passion' : 'Police'
}


# print(Stu)
# {'Name': 'Santhosh', 'Age': 20, 'Country': 'India', 'Marks': 100, 'Passion': 'Police'}

# Update value by using key

# Stu.update({'Name' : 'Madhuri'})
# print(Stu)


# Without using inbuilt method , how you will change a value of specified key

# sy : dict[key] = 'New value'

Stu['Name'] = 'Ajay'
print(Stu)
# {'Name': 'Ajay', 'Age': 20, 'Country': 'India', 'Marks': 100, 'Passion': 'Police'}


Stu['Passion'] = 'Doctor'
print(Stu)
# {'Name': 'Ajay', 'Age': 20, 'Country': 'India', 'Marks': 100, 'Passion': 'Doctor'}

