
# Without using third variable

# a = 5
# b = 10
#
# a = a + b
# b = a - b
# a = a - b

# print(a/b)


# a = 0
# b = 1
# num = 10
# print(a)
# print(b)
# while num - 2:
#     temp = a + b
#     a = b
#     b = temp
#     print(temp)
#     num = num -1


Fname = "yoge"
Lname = 'swar'
print(f'before swap fname : {Fname}')
print(f'before swap lname : {Lname}')
#swapping in single line
Fname,Lname = Lname,Fname
print(f'After swap fname : {Fname}')
print(f'After swap lname : {Lname}')

# before swap fname : yoge
# before swap lname : swar
# After swap fname : swar
# After swap lname : yoge
