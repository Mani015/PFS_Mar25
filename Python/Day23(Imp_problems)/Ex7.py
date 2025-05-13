
def is_prime(n):
    if n <= 1:               
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:       
            return False
    return True              

num = [10, 23, 5, 6, 8, 3, 12, 17, 34, 29, 50]

prime_count = 0             

for n in num:               
    if is_prime(n):         
        prime_count += 1    
print("Number of prime numbers:",prime_count)



