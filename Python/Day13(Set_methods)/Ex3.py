
# The intersection() method returns a set that contains the similarity between two or more sets.

# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.


num1 = {1,2,3,4,5,6,7}

num2 = {7,6,2,8,9,10}

# syn : set1.intersection(set2)

print(num1.intersection(num2))
# {2, 6, 7}



num1.intersection_update(num2)

print('set num1 values : ', num1)

# set num1 values :  {2, 6, 7}


