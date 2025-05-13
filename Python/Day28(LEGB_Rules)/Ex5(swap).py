# Swapping of two values

x = 3
y = 5

# Swapping with 3rd variable
z = x
x = y
y = z

print(x - y)
# -2


# Swapping with in single line

Fname = "bhanu"
Lname = 'Rizwana'

print(f'Before Fname : {Fname}, Before Lname : {Lname}' )

Lname, Fname = Fname,Lname
print(f'After Fname : {Fname}, After Lname : {Lname}' )
# Before Fname : bhanu, Before Lname : Rizwana
# After Fname : Rizwana, After Lname : bhanu


a = 10
b = 2
a = a + b  # 12
b = a - b #10
a = a - b # 2
print(a/b)  # 5.0

# 0.2
