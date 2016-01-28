# Euler 010
def isPrime(num):
    """determine if this number is a prime"""
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
sum = 2
for i in range(3,2000000,2):
    if isPrime(i):
        sum += i
print sum