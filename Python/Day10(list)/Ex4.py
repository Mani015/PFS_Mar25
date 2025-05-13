
fruits  : list[str] = ['apple','mango','orange','guava','watermelon','graphes']

# if you want remove a specified value from the list using remove method
# syn : list.remove(object/value)

fruits.remove('mango')

# print(fruits)  ['apple', 'orange', 'guava', 'watermelon', 'graphes']

fruits.remove('watermelon')
# print(fruits)  ['apple', 'orange', 'guava', 'graphes']


# Incase, if you try to remove a specified value (doesnt exist)

# fruits.remove('banana')
# ValueError: list.remove(x): x not in list



Students : list[str] = ['Raju','sumanth','vishal','varun','vijay']
# pop  : removes a particular index position value
# syntax : list.pop(index)

Students.pop(1)
print(Students)
# ['Raju', 'vishal', 'varun', 'vijay']


Students.pop(3)
print(Students)
# ['Raju', 'vishal', 'varun']


# Case 2 : if you don't provide index value, By defaultly it removes -1 index position 

print()

Students.pop()

print(Students)
# ['Raju', 'vishal']
