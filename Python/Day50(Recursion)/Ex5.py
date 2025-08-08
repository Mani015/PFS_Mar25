def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
# for i in range(10):
#     print(f"Fibonacci({i}) = {fibonacci(i)}")

# Fibonacci(0) = 0
# Fibonacci(1) = 1
# Fibonacci(2) = 1
# Fibonacci(3) = 2
# Fibonacci(4) = 3
# Fibonacci(5) = 5
# Fibonacci(6) = 8
# Fibonacci(7) = 13
# Fibonacci(8) = 21
# Fibonacci(9) = 34



# swapping : To interchange the values

# With temparory value
a = 5
b = 10

temp = a
a = b
b = temp
print(a/b)
# 2.0

