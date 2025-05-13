
# Special Number 
# 19    -->   1 * 9  = 9
# 19    -->   1 + 9  = 10
# -------------------------
                     # 19


num = int(input('Enter a number : '))

print(num)



digit1 = num % 10
# 10) 19 (1
#     10
#   -----
#     9

digit2 = num // 10


print('Special number' if (digit1 + digit2) * (digit1 * digit2) == num else 'Not a Special number' )

# 10 ) 29 (2
#      20

# Enter a number : 39
# 39
# Special number


# Enter a number : 45
# 45
# Not a Special number


