

players = {'virat','rohit sharma','Iyer','KL rahul','Pandya','shami','yadav','patel'}

# copy : shallow copy into a new set

Indian = set({})

Indian = players.copy()
# print(Indian)

# {'rohit sharma', 'virat', 'shami', 'KL rahul', 'Pandya', 'patel', 'Iyer', 'yadav'}



s1 = {1,2,3,4,5}
s2 = {6,7,8,9,0}

print(s1.union(s2))

s3 = {2,3,7,8,9}

print(s3.union(s1))
# {1, 2, 3, 4, 5, 7, 8, 9}


# print(help(set))
