# Euler 012
def calFactors(n):
    factors = []
    for i in range(1,(int(n**0.5)+1)):
        if n % i == 0:
            factors.extend([i, n/i])
    factors = list(set(factors))
    #factors.sort()
    return len(factors)

divisors = 0
i = 1
triNum = 0
while divisors < 500:
    i += 1
    triNum = reduce(lambda x,y:x+y, range(0,i))
    divisors = calFactors(triNum)
print triNum