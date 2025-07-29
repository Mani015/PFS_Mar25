
import sys
def Table(num):

    list_display = []

    for i in range(1,11):

        list_display.append(f"{num} x {i} = {num * i}")

    return list_display

ob1 = Table(num=int(input('Enter your number : ')))
# print(ob1)

print(f'return allocate memory  : {sys.getsizeof(ob1)}')
# for k in ob1:
#     print(k)




def Table2(num):

    for i in range(1,11):
        yield f"{num} x {i} = {num * i}"

ob2 = Table2(num = int(input('Enter a number : ')))
# print(ob2)

# for k in ob2:
#     print(k)
print(f'yield allocate memory  : {sys.getsizeof(ob2)}')