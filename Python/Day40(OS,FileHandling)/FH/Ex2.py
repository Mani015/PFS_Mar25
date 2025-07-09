
# file = open('info.txt','w')
# write = file.write("Hello, Yogeswar")
# print(write)
# file.close()


# file = open('info.txt','w')
# write = file.write("Hello, Simhadri")
# print(write)
# file.close()



new = open('info.txt','r')
read1 = new.read()
# print(read1)
# Hello, Simhadri

# print('file, is it closed or not ? :', new.closed)
# file, is it closed or not ? : False

# new.close()
# print('file, is it closed or not ? :', new.closed)
# file, is it closed or not ? : True

x = open('info.txt','w')
x.write('My name is Meghana')
print(x)
x.close()
x.write("My name is Bhanu prasad")
print(x)
# ValueError: I/O operation on closed file.


