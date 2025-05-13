
# Set is a unordered(shuffle) datatype, it mean doesn't have indexing values

s1 = {5,10,15,20,25,96,40}

# print(s1)

# Set doesn't allows duplicate values(repeated values) Unique values

s2 = {'suneel','pawan','srikanth','ramesh','suresh','vamsi','pawan','ramesh'}
# print(s2)
# {'vamsi', 'ramesh', 'suresh', 'pawan', 'suneel', 'srikanth'}



# set is it mutable or Immutable ?
# Set is Mutable datatype it can add or remove the elements

# add : adding a new element into a set
# sy : set.add(element)

s2.add('samuel')

# print(s2)

# Adding more than one value 

# s2.add('stephen','David')
# print(s2)
# TypeError: set.add() takes exactly one argument (2 given)


# syn : set.update(object)
# update : adding more than one elements to the set
Names = {'Banana','apple','Guava','orange','pineapple','Graphes'}
print(Names)

Names.update({'Mango','kiwi'})
print(Names)

# {'apple', 'Banana', 'orange', 'Graphes', 'pineapple', 'Guava', 'Mango', 'kiwi'}


x  : list = ['dragon fruit','watermelon']


Names.update(x)
print(Names)

# {'pineapple', 'Banana', 'dragon fruit', 'Mango', 'kiwi', 'Guava', 'apple', 'orange', 'watermelon', 'Graphes'}












