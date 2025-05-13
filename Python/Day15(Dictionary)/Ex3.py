
# Extract value by their key

info = {
	'Name' : 'sudheer',
	'Age' : 20,
	'location' : 'chennai',
	'phone' : 12345678

}

# print(info)


# sy : dict[key]

# print(info['Name']) sudheer

# print(info['Age']) 20

# print(info['location']) chennai

# print(info['phone'])12345678


# Extract all values
# dict.values

print(info.values())
# dict_values(['sudheer', 20, 'chennai', 12345678])


# Extract all kesy

print(info.keys())
# dict_keys(['Name', 'Age', 'location', 'phone'])




# Items : dict.items()

print(info.items())
# dict_items([('Name', 'sudheer'), ('Age', 20), ('location', 'chennai'), ('phone', 12345678)])
