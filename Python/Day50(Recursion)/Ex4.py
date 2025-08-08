

def Factorial(num):

    if num == 0:
        return 1

    else:

        return num * Factorial(num - 1)

# print(Sum_of_num(10))


for i in range(1,11):
    print(f'factorial of : {i} is {Factorial(i)}')


# factorial of : 1 is 1
# factorial of : 2 is 2
# factorial of : 3 is 6
# factorial of : 4 is 24
# factorial of : 5 is 120
# factorial of : 6 is 720
# factorial of : 7 is 5040
# factorial of : 8 is 40320
# factorial of : 9 is 362880
# factorial of : 10 is 3628800
