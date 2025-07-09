
r1 = open('info.txt','r')
r1.seek(10)
print('cursor point : ',r1.tell()) # cursor point :  10
print(r1.read(7))

print('cursor point : ',r1.tell())
# cursor point :  10
# cond li
# cursor point :  17
