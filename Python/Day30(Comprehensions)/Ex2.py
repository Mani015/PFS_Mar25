

l1  = [2,3,45,6,9,9,6,3,2,4,5,6,7,9,9,5,2,1,3,5,7,9,0]

# dict1 = {2 : 3, 3 : 3}

new_dict = {}

for k in l1:

    if k not in new_dict:
        new_dict[k] = 1


    else:
        new_dict[k] += 1

print(new_dict)
# {2: 3, 3: 3, 45: 1, 6: 3, 9: 5, 4: 1, 5: 3, 7: 2, 1: 1, 0: 1}
