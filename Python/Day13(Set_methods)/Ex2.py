
# The difference_update() method removes the items that exist in both sets.

# The difference_update() method is different from the difference() method,
# because the difference() method returns a new set, without the unwanted items,
# and the difference_update() method removes the unwanted items from the original set.


heros = {'ramcharan','prabhash','allu arjun','ntr','mahesh','nani'}

telugu_heros = {'balakrishna','chiranjeevi','vijay','dhanush','siddu','nani','ntr','mahesh'}

print('Before set1 values : ', heros)

# print(heros.difference(telugu_heros))
# {'prabhash', 'ramcharan', 'allu arjun'}

heros.difference_update(telugu_heros)

print('After set1 values : ', heros)
# After set1 values :  {'allu arjun', 'prabhash', 'ramcharan'}
