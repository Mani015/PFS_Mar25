
# difference :
# The difference() method returns a set that contains the difference between two sets.

# Meaning: The returned set contains items that exist only in the first set, and not in both sets.

team1 = {'Bharath','yogeswar','suryaprakash','suresh'}

team2 = {'Thulasi','Priya','yogeswar','madhuri','reddy pasand'}

# syntax :  set1.difference(set2)

print('differnec values of set1 : ', team1.difference(team2))

# differnec values of set1 :  {'suresh', 'suryaprakash', 'Bharath'}



print('differnec values of set2 : ', team2.difference(team1))
# differnec values of set2 :  {'Priya', 'Thulasi', 'madhuri', 'reddy pasand'}
