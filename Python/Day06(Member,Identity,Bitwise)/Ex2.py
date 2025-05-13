
# Identity operator
# Identity operators are used to compare the objects, not if they are equal,
 # but if they are actually the same object, with the same memory location:


# is : Return True, if the both objects are same

name1 = "pavani"
# print(id(name1))

name2  = 'pavani'
# print(id(name2))

# print(name1 is name2)  True


num1 = [1,2,3,4,5]

num2 = [1,2,3,4,5]
print('id of num1 : ',id(num1))
print('id of num2 : ',id(num2))

num3 = num1
print('id of num3 : ',id(num3))
print(num1,num2)
# [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]

num3.append(6)

print()
print(num1,num3)
# [1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5, 6]

print(num1 is num3)
