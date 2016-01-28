# Euler 007
# Find 10001 prime number

# function to define primer
def isPrime(num):
    """determine if this number is a prime"""
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

i = 1
counter = 1
while counter < 10001:
    i += 2
    if isPrime(i):
        counter += 1
print i
print counter