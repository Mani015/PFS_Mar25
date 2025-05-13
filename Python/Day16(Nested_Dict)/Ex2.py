# In python dict, key are immutable ('Does not allow duplicate key')

Mobile : dict = {
	'Brand_name' : 'Samsung',
	'Brand_color' : 'Forest green',
	'Brand_cost' : 20000,
	'Processor' : 'snapdragon',
	'Battery' : '5000mah',
	'RAM'    : '6GB'
}


# print(Mobile)
# {'Brand_name': 'Samsung', 'Brand_color': 'Forest green', 'Brand_cost': 20000, 'Processor': 'snapdragon'}


# update key : 

# Mobile.update({'ROM':'6GB'})

# print(Mobile)
# {'Brand_name': 'Samsung', 'Brand_color': 'Forest green', 'Brand_cost': 20000, 'Processor': 'snapdragon', 'Battery': '5000mah', 'RAM': '6GB', 'ROM': '6GB'}


Mobile['ROM'] = Mobile.pop('RAM')

# print(Mobile)

# {'Brand_name': 'Samsung', 'Brand_color': 'Forest green', 'Brand_cost': 20000, 'Processor': 'snapdragon', 'Battery': '5000mah', 'ROM': '6GB'}



Mobile['Mobile_color']  = Mobile.pop('Brand_color')

print(Mobile)
# {'Brand_name': 'Samsung', 'Brand_cost': 20000, 'Processor': 'snapdragon', 'Battery': '5000mah', 'ROM': '6GB', 'Mobile_color': 'Forest green'}

