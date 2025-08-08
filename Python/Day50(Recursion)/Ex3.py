
# - Add a base case: Make sure your recursive function has a termination condition.


# Sum of list range number

def Sum_of_num(num):

    if num == 0:
        return 0

    else:

        return num + Sum_of_num(num - 1)

# print(Sum_of_num(10))


for i in range(1,11):
    print(f'factorial of : {i} is {Sum_of_num(i)}')



# factorial of : 1 is 1
# factorial of : 2 is 3
# factorial of : 3 is 6
# factorial of : 4 is 10
# factorial of : 5 is 15
# factorial of : 6 is 21
# factorial of : 7 is 28
# factorial of : 8 is 36
# factorial of : 9 is 45
# factorial of : 10 is 55