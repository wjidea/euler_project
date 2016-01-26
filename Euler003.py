def get_prime_factor(n):
    prime = []
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            prime.append(i)
            while n % i == 0:
                n /= i
    if len(prime) == 0:  # prime
        prime.append(n)
    return prime


print get_prime_factor(600851475143)[-1]