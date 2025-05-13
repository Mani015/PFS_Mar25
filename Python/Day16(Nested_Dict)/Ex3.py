
# Nested Dict : A nested dictionary it contains multiple dictionary's


Stu_info : dict = {
	
	'Roll_1' : {'Name' : 'Vikram','Age' : 24, 'Marks' : 100},
	'Roll_2' : {'Name' : 'Chakri','Age' : 23, 'Marks' : 99},
	'Roll_3' : {'Name' : 'Bharath','Age' : 21, 'Marks' : 98}
}

# Extract all keys of Stu_info 
# print(Stu_info.keys())
# dict_keys(['Roll_1', 'Roll_2', 'Roll_3'])

# Extract all kesy of   (key of Roll_1)  of Stu_info

x = Stu_info.get('Roll_1')
# print(type(x))
# print(x.keys())dict_keys(['Name', 'Age', 'Marks'])
# print(x.values()) dict_values(['Vikram', 24, 100])
# print(x.items()) 
# dict_items([('Name', 'Vikram'), ('Age', 24), ('Marks', 100)])

print()

y = Stu_info.get('Roll_2')

print(y.keys())
print(y.values())
print(y.items())
# dict_keys(['Name', 'Age', 'Marks'])
# dict_values(['Chakri', 23, 99])
# dict_items([('Name', 'Chakri'), ('Age', 23), ('Marks', 99)])


print()

z = Stu_info.get('Roll_3')

print(z.keys())
print(z.values())
print(z.items())
# dict_keys(['Name', 'Age', 'Marks'])
# dict_values(['Bharath', 21, 98])
# dict_items([('Name', 'Bharath'), ('Age', 21), ('Marks', 98)])

